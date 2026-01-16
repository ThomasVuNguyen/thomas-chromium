#!/bin/bash
# Thomas Chromium - Build Script (Shell wrapper)
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLATFORM="${1:-linux}"

echo "=== Thomas Chromium Build - $PLATFORM ==="

python3 "$SCRIPT_DIR/build.py" "$PLATFORM"
