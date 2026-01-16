#!/bin/bash
# Thomas Chromium - Setup Script (Shell wrapper)
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLATFORM="${1:-linux}"

echo "=== Thomas Chromium Setup - $PLATFORM ==="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required"
    exit 1
fi

# Run Python setup script
python3 "$SCRIPT_DIR/setup.py" "$PLATFORM"
