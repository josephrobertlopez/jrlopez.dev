#!/usr/bin/env python3
"""
forge.py — jrlopez.dev build pipeline

Core responsibilities:
  L1: Extract HTML → text (strip tags, preserve structure)
  L2: Generate .md companions with YAML frontmatter (from index.json metadata)
  L3: Rebuild discovery files (llms-full.txt, sitemap.xml, llms.txt)
  L4: Validate via BDD gate (delegated to behave)
  L5: Stage generated files for commit

Usage:
  python build/forge.py build           # Full build
  python build/forge.py build --dry-run # Show what would change
  python build/forge.py clean           # Remove generated .md
  python build/forge.py discovery       # Rebuild discovery files only
"""

import sys
import json
import re
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser
from xml.etree.ElementTree import Element, ElementTree
from typing import Optional, Dict, Set, Tuple, Any


# ============================================================================
# CONFIGURATION
# ============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
INDEX_JSON_PATH = PROJECT_ROOT / "index.json"
P_DIR = PROJECT_ROOT / "p"
BUILD_DIR = PROJECT_ROOT / "build"
STATE_FILE = BUILD_DIR / ".build-state.json"
LLMS_FULL_PATH = PROJECT_ROOT / "llms-full.txt"
SITEMAP_PATH = PROJECT_ROOT / "sitemap.xml"
LLMS_TXT_PATH = PROJECT_ROOT / "llms.txt"

# Hand-authored skills that should never be auto-regenerated
PROTECTED_MD_FILES = {
    "skills-dev-second-brain.md",
    "skills-po-second-brain.md",
    "skills-dl-second-brain.md",
    "skills-tl-second-brain.md",
    "skills-make-skills.md",
}


# ============================================================================
# HTML PARSER
# ============================================================================

class HTMLToMarkdown(HTMLParser):
    """Extract text from HTML and convert to markdown structure."""

    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.tag_stack = []
        self.in_article = False
        self.in_code = False
        self.in_blockquote = False
        self.in_list = False
        self.list_level = 0
        self.after_style_close = False

    def handle_starttag(self, tag: str, attrs: list):
        """Track opening tags."""
        if tag == "article":
            self.in_article = True
        elif tag == "style":
            self.after_style_close = False
        elif tag == "script":
            self.tag_stack.append("script")
            return
        elif tag in ("nav", "footer"):
            return
        elif tag in ("code", "pre"):
            self.in_code = True
            if tag == "pre":
                self.text_parts.append("\n```\n")
        elif tag == "blockquote":
            self.in_blockquote = True
            self.text_parts.append("> ")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self.text_parts.append(f"\n{'#' * level} ")
        elif tag == "p":
            if self.text_parts and self.text_parts[-1].strip():
                self.text_parts.append("\n")
        elif tag == "li":
            indent = "  " * self.list_level
            self.text_parts.append(f"\n{indent}- ")
        elif tag == "ul" or tag == "ol":
            self.list_level += 1
            self.in_list = True
        elif tag == "strong" or tag == "b":
            self.text_parts.append("**")
        elif tag == "em" or tag == "i":
            self.text_parts.append("*")
        elif tag == "a":
            self.text_parts.append("[")
        elif tag == "table":
            self.text_parts.append("\n")
        elif tag == "tr":
            self.text_parts.append("\n")
        elif tag == "td" or tag == "th":
            self.text_parts.append("| ")
        elif tag == "br":
            self.text_parts.append("\n")

        self.tag_stack.append(tag)

    def handle_endtag(self, tag: str):
        """Track closing tags."""
        if tag == "article":
            self.in_article = False
        elif tag == "style":
            self.after_style_close = True
        elif tag == "script":
            if self.tag_stack and self.tag_stack[-1] == "script":
                self.tag_stack.pop()
            return
        elif tag in ("code", "pre"):
            self.in_code = False
            if tag == "pre":
                self.text_parts.append("\n```\n")
        elif tag == "blockquote":
            self.in_blockquote = False
        elif tag == "strong" or tag == "b":
            self.text_parts.append("**")
        elif tag == "em" or tag == "i":
            self.text_parts.append("*")
        elif tag == "a":
            # Attempt to extract href from attrs (stored during start tag)
            self.text_parts.append("]()")
        elif tag in ("ul", "ol"):
            self.list_level = max(0, self.list_level - 1)
            self.in_list = self.list_level > 0
        elif tag == "td" or tag == "th":
            self.text_parts.append(" |")
        elif tag == "tr":
            self.text_parts.append("\n")
        elif tag == "table":
            self.text_parts.append("\n")

        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()

    def handle_data(self, data: str):
        """Handle text content."""
        if not data.strip():
            return
        if self.tag_stack and self.tag_stack[-1] == "script":
            return
        if "nav" in self.tag_stack or "footer" in self.tag_stack:
            return

        # Only include text if we're in article, or after style close
        if self.in_article or self.after_style_close:
            text = data.strip()
            if text:
                self.text_parts.append(text)
                if not (self.in_code or self.in_blockquote):
                    self.text_parts.append(" ")

    def get_text(self) -> str:
        """Return parsed markdown text."""
        text = "".join(self.text_parts)
        # Clean up multiple newlines
        text = re.sub(r"\n\n\n+", "\n\n", text)
        # Clean up spacing around markdown
        text = re.sub(r" \n", "\n", text)
        text = re.sub(r"\n ", "\n", text)
        return text.strip()


def extract_html_content(html_path: Path) -> str:
    """Extract markdown from HTML file."""
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except Exception as e:
        print(f"  ❌ Failed to read {html_path}: {e}")
        return ""

    parser = HTMLToMarkdown()
    try:
        parser.feed(html_content)
    except Exception as e:
        print(f"  ❌ Failed to parse {html_path}: {e}")
        return ""

    text = parser.get_text()
    if not text:
        print(f"  ⚠ No content extracted from {html_path}")
    return text


# ============================================================================
# INDEX & STATE MANAGEMENT
# ============================================================================

def load_index() -> Dict[str, Any]:
    """Load and validate index.json."""
    try:
        with open(INDEX_JSON_PATH, "r") as f:
            index = json.load(f)
        return index
    except Exception as e:
        print(f"❌ Failed to load index.json: {e}")
        sys.exit(1)


def load_build_state() -> Dict[str, str]:
    """Load .build-state.json (hash cache)."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_build_state(state: Dict[str, str]):
    """Save .build-state.json."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def file_hash(path: Path) -> str:
    """Compute MD5 hash of file content."""
    if not path.exists():
        return ""
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


# ============================================================================
# MARKDOWN GENERATION
# ============================================================================

def generate_companion_md(
    html_stem: str,
    html_path: Path,
    atom: Dict[str, Any],
    content: str,
    dry_run: bool = False,
) -> bool:
    """Generate .md companion from HTML + index.json metadata."""
    md_path = P_DIR / f"{html_stem}.md"

    # Check if hand-authored protected file
    if html_stem in [f.replace(".md", "") for f in PROTECTED_MD_FILES]:
        print(f"  ⏭ Skipping protected: {html_stem}.md")
        return True

    # Check if existing .md is hand-authored (missing `generated: true` in frontmatter)
    if md_path.exists():
        try:
            with open(md_path, "r") as f:
                first_block = f.read(500)
            if "generated: true" not in first_block:
                print(f"  ⏭ Skipping hand-authored: {html_stem}.md")
                return True
        except:
            pass

    # Build frontmatter
    title = atom.get("title", "").replace('"', '\\"')
    desc = atom.get("desc", "").replace('"', '\\"')
    date = atom.get("date", "2026-01-01")
    tags = atom.get("tags", [])
    atom_id = atom.get("id", 0)

    frontmatter = f"""---
title: "{title}"
description: "{desc}"
author: "Joey Lopez"
date: "{date}"
tags: {json.dumps(tags)}
atom_id: {atom_id}
source_html: "{html_path.name}"
url: "https://jrlopez.dev/p/{html_stem}.html"
generated: true
---
"""

    full_content = frontmatter + "\n" + content

    if dry_run:
        print(f"  📝 Would write {html_stem}.md ({len(full_content)} bytes)")
        return True

    try:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"  ✅ Generated {html_stem}.md")
        return True
    except Exception as e:
        print(f"  ❌ Failed to write {html_stem}.md: {e}")
        return False


# ============================================================================
# L1-L2: EXTRACT & GENERATE
# ============================================================================

def build_extract_and_generate(dry_run: bool = False) -> bool:
    """L1-L2: Extract HTML → Generate .md companions."""
    print("\n[L1-L2] Extract & Generate")
    print("=" * 60)

    index = load_index()
    state = load_build_state()
    new_state = {}

    success = True

    for atom in index.get("atoms", []):
        html_url = atom.get("html_url", "")
        if not html_url or html_url.startswith("http"):
            # External link or no URL, skip
            continue

        # Strip fragment and "p/" prefix
        html_url = html_url.split("#")[0]
        if html_url.startswith("p/"):
            html_url = html_url[2:]

        # Handle root-level files (e.g. resume.html)
        html_path = P_DIR / html_url
        if not html_path.exists():
            html_path = PROJECT_ROOT / html_url
        if not html_path.exists():
            print(f"  ⚠ Missing: {html_path}")
            continue

        html_stem = html_path.stem
        current_hash = file_hash(html_path)
        new_state[html_stem] = current_hash

        # Check if changed
        if state.get(html_stem) == current_hash and not dry_run:
            print(f"  ⏭ Unchanged: {html_stem}.html")
            continue

        print(f"  📂 {html_stem}.html")

        # L1: Extract
        content = extract_html_content(html_path)
        if not content:
            success = False
            continue

        # L2: Generate
        if not generate_companion_md(html_stem, html_path, atom, content, dry_run):
            success = False

    # Save state
    if not dry_run:
        save_build_state(new_state)

    return success


# ============================================================================
# L3A: REBUILD llms-full.txt
# ============================================================================

def rebuild_llms_full(dry_run: bool = False) -> bool:
    """L3a: Concatenate all .md files into llms-full.txt."""
    print("\n[L3a] Rebuild llms-full.txt")
    print("=" * 60)

    index = load_index()
    sections = []

    header = f"""# Joey Lopez — Knowledge Base
Generated: {datetime.now().isoformat()}
Base URL: https://jrlopez.dev/

This file aggregates all public knowledge from jrlopez.dev.
Source: index.json (single source of truth)
---

"""
    sections.append(header)

    # Collect all .md files from p/
    md_files = sorted(P_DIR.glob("*.md"))
    if not md_files:
        print("  ⚠ No .md files found in p/")
        return False

    for md_path in md_files:
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract atom_id from frontmatter if present
            atom_id_match = re.search(r'atom_id: (\d+)', content)
            atom_id = int(atom_id_match.group(1)) if atom_id_match else 999

            # Extract URL from frontmatter
            url_match = re.search(r'url: "(.*?)"', content)
            url = url_match.group(1) if url_match else f"https://jrlopez.dev/p/{md_path.stem}.md"

            sections.append(f"\n---\n# {md_path.name}\n# {url}\n\n")
            sections.append(content)
        except Exception as e:
            print(f"  ❌ Failed to read {md_path}: {e}")
            return False

    full_content = "".join(sections)

    if dry_run:
        print(f"  📝 Would write llms-full.txt ({len(full_content)} bytes)")
        return True

    try:
        with open(LLMS_FULL_PATH, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"  ✅ Generated llms-full.txt ({len(full_content)} bytes)")
        return True
    except Exception as e:
        print(f"  ❌ Failed to write llms-full.txt: {e}")
        return False


# ============================================================================
# L3B: REBUILD sitemap.xml
# ============================================================================

def rebuild_sitemap(dry_run: bool = False) -> bool:
    """L3b: Generate sitemap.xml from index.json."""
    print("\n[L3b] Rebuild sitemap.xml")
    print("=" * 60)

    index = load_index()
    base_url = index.get("base_url", "https://jrlopez.dev/")

    urlset = Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    # Add root
    url_elem = Element("url")
    loc = Element("loc")
    loc.text = base_url
    url_elem.append(loc)
    lastmod = Element("lastmod")
    lastmod.text = datetime.now().strftime("%Y-%m-%d")
    url_elem.append(lastmod)
    urlset.append(url_elem)

    # Add resume
    url_elem = Element("url")
    loc = Element("loc")
    loc.text = f"{base_url}resume.html"
    url_elem.append(loc)
    lastmod = Element("lastmod")
    lastmod.text = "2026-03-24"
    url_elem.append(lastmod)
    urlset.append(url_elem)

    # Add atoms (deduplicate by URL after stripping fragments)
    seen_urls: Set[str] = {base_url, f"{base_url}resume.html"}
    for atom in index.get("atoms", []):
        html_url = atom.get("html_url", "")
        if not html_url:
            continue

        # Build full URL — strip fragments, use path as-is from index.json
        html_url = html_url.split("#")[0]
        if html_url.startswith("http"):
            full_url = html_url
        else:
            full_url = f"{base_url}{html_url}"

        if full_url in seen_urls:
            continue
        seen_urls.add(full_url)

        url_elem = Element("url")
        loc = Element("loc")
        loc.text = full_url
        url_elem.append(loc)

        # Add lastmod if date exists
        date = atom.get("date")
        if date:
            lastmod = Element("lastmod")
            lastmod.text = date
            url_elem.append(lastmod)

        urlset.append(url_elem)

    if dry_run:
        tree = ElementTree(urlset)
        import io
        buf = io.StringIO()
        tree.write(buf, encoding="unicode", xml_declaration=True)
        print(f"  📝 Would write sitemap.xml ({len(buf.getvalue())} bytes)")
        return True

    try:
        tree = ElementTree(urlset)
        tree.write(SITEMAP_PATH, encoding="utf-8", xml_declaration=True)
        print(f"  ✅ Generated sitemap.xml")
        return True
    except Exception as e:
        print(f"  ❌ Failed to write sitemap.xml: {e}")
        return False


# ============================================================================
# L3C: REBUILD llms.txt
# ============================================================================

def rebuild_llms_txt(dry_run: bool = False) -> bool:
    """L3c: Generate llms.txt (curated summary) from index.json."""
    print("\n[L3c] Rebuild llms.txt")
    print("=" * 60)

    index = load_index()
    name = index.get("name", "Joey Lopez")
    description = index.get("description", "")
    base_url = index.get("base_url", "https://jrlopez.dev/")

    # Group atoms by primary tag
    tag_groups: Dict[str, list] = {}
    for atom in index.get("atoms", []):
        if not atom.get("html_url"):
            continue
        primary_tag = atom.get("tags", [None])[0] or "other"
        if primary_tag not in tag_groups:
            tag_groups[primary_tag] = []
        tag_groups[primary_tag].append(atom)

    # Build llms.txt content
    lines = [
        f"# {name}\n",
        f"> {description}\n",
    ]

    # Add each tag group
    for tag in sorted(tag_groups.keys()):
        # Capitalize tag for header
        header = tag.replace("-", " ").title()
        lines.append(f"\n## {header}\n")

        atoms = sorted(tag_groups[tag], key=lambda a: a.get("date", ""), reverse=True)
        for atom in atoms:
            title = atom.get("title", "")
            desc = atom.get("desc", "")
            html_url = atom.get("html_url", "")

            # Build full URL
            if html_url.startswith("http"):
                full_url = html_url
            else:
                # Ensure we have p/ prefix for local files
                if not html_url.startswith("p/"):
                    full_url = f"{base_url}p/{html_url}"
                else:
                    full_url = f"{base_url}{html_url}"

            lines.append(f"\n- [{title}]({full_url}): {desc}\n")

    # Add contact section
    lines.append("\n## Contact\n")
    lines.append("\n- Email: josephrobertlopez@gmail.com\n")
    lines.append("- GitHub: https://github.com/josephrobertlopez\n")
    lines.append("- LinkedIn: https://www.linkedin.com/in/joseph-lopez-80aa81166/\n")
    lines.append("- Calendly: https://calendly.com/josephrobertlopez\n")

    content = "".join(lines)

    if dry_run:
        print(f"  📝 Would write llms.txt ({len(content)} bytes)")
        return True

    try:
        with open(LLMS_TXT_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ Generated llms.txt")
        return True
    except Exception as e:
        print(f"  ❌ Failed to write llms.txt: {e}")
        return False


# ============================================================================
# CLEAN: Remove generated .md files
# ============================================================================

def clean_generated_md() -> bool:
    """Remove all generated .md files (keep hand-authored ones)."""
    print("\n[CLEAN] Remove generated .md files")
    print("=" * 60)

    index = load_index()
    count = 0

    for atom in index.get("atoms", []):
        html_url = atom.get("html_url", "")
        if not html_url or html_url.startswith("http"):
            continue

        # Strip "p/" prefix if present
        if html_url.startswith("p/"):
            html_url = html_url[2:]

        html_stem = Path(html_url).stem
        md_path = P_DIR / f"{html_stem}.md"

        if not md_path.exists():
            continue

        # Check if it's protected
        if html_stem in [f.replace(".md", "") for f in PROTECTED_MD_FILES]:
            print(f"  ⏭ Protected: {html_stem}.md")
            continue

        # Check if generated
        try:
            with open(md_path, "r") as f:
                content = f.read(500)
            if "generated: true" in content:
                md_path.unlink()
                print(f"  🗑 Removed {html_stem}.md")
                count += 1
            else:
                print(f"  ⏭ Hand-authored: {html_stem}.md")
        except Exception as e:
            print(f"  ⚠ Failed to check {html_stem}.md: {e}")

    print(f"\n  ✅ Cleaned {count} generated .md files")
    return True


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="jrlopez.dev build pipeline (forge)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  build           Full build: extract + generate + rebuild indexes
  build --dry-run Show what would change without writing
  clean           Remove generated .md files (keep hand-authored ones)
  discovery       Rebuild discovery files only (llms-full.txt, sitemap.xml, llms.txt)
        """,
    )

    parser.add_argument(
        "command",
        choices=["build", "clean", "discovery"],
        help="Build command",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing",
    )

    args = parser.parse_args()

    print(f"\n🔨 forge.py — jrlopez.dev build pipeline")
    print(f"   Command: {args.command}")
    if args.dry_run:
        print(f"   Mode: DRY RUN (no files written)")

    # Ensure directories exist
    P_DIR.mkdir(parents=True, exist_ok=True)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    try:
        if args.command == "build":
            success = (
                build_extract_and_generate(args.dry_run)
                and rebuild_llms_full(args.dry_run)
                and rebuild_sitemap(args.dry_run)
                and rebuild_llms_txt(args.dry_run)
            )
            if success:
                print("\n✅ Build complete")
            else:
                print("\n❌ Build had errors")
                sys.exit(1)

        elif args.command == "clean":
            success = clean_generated_md()
            if success:
                print("\n✅ Clean complete")
            else:
                print("\n❌ Clean had errors")
                sys.exit(1)

        elif args.command == "discovery":
            success = (
                rebuild_llms_full(args.dry_run)
                and rebuild_sitemap(args.dry_run)
                and rebuild_llms_txt(args.dry_run)
            )
            if success:
                print("\n✅ Discovery rebuild complete")
            else:
                print("\n❌ Discovery rebuild had errors")
                sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n⚠ Build interrupted")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
