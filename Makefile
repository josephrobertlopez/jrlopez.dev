# jrlopez.dev build pipeline
# Single source of truth: index.json
# Logic: build/forge.py
# Tests: features/site_coherence.feature

.PHONY: build validate clean install-hooks all

PYTHON ?= python3
FORGE  := build/forge.py
STATE  := build/.build-state.json

all: build validate

# L1-L3: Extract, generate, rebuild
build:
	$(PYTHON) $(FORGE) build

# L4: BDD validation gate
validate:
	$(PYTHON) -m behave features/ --no-capture --format progress

# Wipe generated .md companions and rebuild artifacts
clean:
	$(PYTHON) $(FORGE) clean
	rm -f $(STATE)

# One-time: install pre-commit hook
install-hooks:
	mkdir -p .githooks
	cp build/pre-commit .githooks/pre-commit
	chmod +x .githooks/pre-commit
	git config core.hooksPath .githooks
	@echo "Pre-commit hook installed."

# Show what would change without writing
dry-run:
	$(PYTHON) $(FORGE) build --dry-run

# Rebuild only agent discovery files (skip .md generation)
discovery:
	$(PYTHON) $(FORGE) discovery
