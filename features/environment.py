"""
BDD environment setup for site coherence tests.
Initializes shared context for all scenarios.
"""
import json
import os
from pathlib import Path


def before_all(context):
    """Set up shared context for all scenarios."""
    # Determine site root: go up 2 levels from features/
    features_dir = Path(__file__).parent
    site_root = features_dir.parent.absolute()
    context.site_root = site_root

    # Load index.json
    index_path = site_root / "index.json"
    with open(index_path) as f:
        index_data = json.load(f)

    context.index_data = index_data
    context.atoms = index_data.get("atoms", [])
    context.atom_tags = index_data.get("tags", [])  # Renamed to avoid conflict with behave's context.tags
    context.base_url = index_data.get("base_url", "https://jrlopez.dev/")
    context.schema_version = index_data.get("schema", "jrlopez-atom-index/1.0")

    # Initialize result tracking
    context.errors = []
    context.orphans = []
    context.missing_companions = []
    context.missing_frontmatter = []
    context.invalid_json_ld = []
    context.broken_links = []
    context.schema_violations = []
