#!/bin/bash
# Local dev server — preview site at http://localhost:60080
# Runs forge build first, then serves
python3 build/forge.py build && python3 -m http.server 60080
