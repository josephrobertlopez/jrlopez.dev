Feature: Site Coherence
  The jrlopez.dev build pipeline must maintain structural integrity
  across index.json, HTML pages, markdown companions, agent discovery
  files, and sitemap. Every atom is reachable. Every page has a
  companion. Every index is complete.

  Background:
    Given the site root is the repository root
    And index.json is loaded as the atom catalog
    And the base_url is "https://jrlopez.dev/"

  # --- Atom Integrity ---

  Scenario: Every atom in index.json resolves to an existing file
    Given all atoms from index.json
    When I check each atom's html_url
    Then every local html_url should resolve to an existing file
    And every external html_url should be a valid URL format
    And fragment-only urls like "#tab-dev" should resolve to an existing base file

  Scenario: No orphan HTML files in p/
    Given all .html files in the p/ directory
    When I compare them against html_url values in index.json
    Then every .html file should be referenced by at least one atom
    And any unreferenced .html file should be reported as orphan

  # --- Markdown Companions ---

  Scenario: Every local HTML page has a companion .md file
    Given all atoms with local html_url pointing to p/*.html
    When I check for a companion .md file with matching stem
    Then every such atom should have a .md file in p/
    And atoms with external html_url are excluded from this check

  Scenario: Every .md companion has valid frontmatter
    Given all .md files in the p/ directory
    When I parse the YAML frontmatter of each file
    Then every .md file should have a "title" field
    And every .md file should have a "date" field matching ISO format
    And every .md file should have a "tags" field that is a list
    And every .md file should have a "source_html" field

  Scenario: Skill .md files have skill-specific frontmatter
    Given all .md files in p/ matching "skills-*.md"
    When I parse the YAML frontmatter of each file
    Then every skill .md should have a "name" field
    And every skill .md should have a "description" field
    And every skill .md should have a "version" field

  # --- Agent Discovery ---

  Scenario: llms-full.txt contains content from every .md file
    Given all .md files in the p/ directory
    And the file llms-full.txt exists at the site root
    When I check llms-full.txt for a section header matching each .md title
    Then every .md file's title should appear as a section in llms-full.txt
    And llms-full.txt should contain zero raw HTML tags
    And llms-full.txt should have a generation timestamp in the header

  Scenario: llms.txt references every content section
    Given the file llms.txt exists at the site root
    When I parse the markdown links in llms.txt
    Then every local atom in index.json should have a corresponding link
    And no link in llms.txt should point to a non-existent local file

  # --- Sitemap ---

  Scenario: sitemap.xml has an entry for every local page
    Given the file sitemap.xml exists at the site root
    When I extract all loc entries from sitemap.xml
    Then there should be an entry for the root URL
    And there should be an entry for resume.html
    And every atom with a local html_url should have a sitemap entry
    And every sitemap entry should have a lastmod element
    And no sitemap entry should reference a non-existent local file

  # --- JSON-LD Structured Data ---

  Scenario: Every HTML page in p/ has valid JSON-LD
    Given all .html files in the p/ directory
    When I extract the JSON-LD script block from each file
    Then every .html file should have exactly one JSON-LD block
    And every JSON-LD block should parse as valid JSON
    And every JSON-LD block should have an "@type" field
    And every JSON-LD block should have a "name" field

  Scenario: JSON-LD metadata is consistent with index.json
    Given all atoms with local html_url pointing to p/*.html
    When I compare the JSON-LD "name" field with the atom "title"
    And I compare the JSON-LD "description" with the atom "desc"
    Then the JSON-LD name should contain key words from the atom title
    And the JSON-LD description should not be empty

  # --- Internal Links ---

  Scenario: All internal links in HTML pages resolve
    Given all .html files in the p/ directory
    When I extract all href values starting with "p/" or ending in ".html"
    And I extract all href values starting with "../" or "./"
    Then every internal link should resolve to an existing file
    And no internal link should return a fragment-only reference to a missing anchor

  # --- Index.json Schema ---

  Scenario: index.json passes schema validation
    Given index.json is loaded
    Then it should have a "schema" field matching "jrlopez-atom-index/1.0"
    And it should have a "total" field matching the count of atoms
    And every atom should have fields: id, title, desc, html_url, tags, date
    And every atom id should be unique
    And every atom date should match ISO 8601 format
    And the "tags" array should contain only tags listed in the top-level tags array

  # --- Build State ---

  Scenario: Generated files are not stale
    Given the build state file .build-state.json exists
    When I compare each .html file's hash against the stored hash
    Then every .html file with a changed hash should have a regenerated .md companion
    And the .build-state.json should contain an entry for every .html in p/
