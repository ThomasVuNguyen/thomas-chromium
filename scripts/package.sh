#!/bin/bash
# Thomas Chromium - Package Script
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
PLATFORM="${1:-linux}"
VERSION="1.0.0"

echo "=== Thomas Chromium Package - $PLATFORM ==="

SRC_DIR="$ROOT_DIR/src"
BUILD_DIR="$SRC_DIR/out/Release"
OUT_DIR="$ROOT_DIR/out"

mkdir -p "$OUT_DIR"

case "$PLATFORM" in
    linux)
        echo "Creating Linux tarball..."
        cd "$BUILD_DIR"
        tar -czvf "$OUT_DIR/thomas-chromium-$VERSION-linux-x64.tar.gz" \
            chrome \
            chrome_sandbox \
            chrome_crashpad_handler \
            *.pak \
            *.dat \
            *.bin \
            locales/ \
            resources/
        echo "Package: $OUT_DIR/thomas-chromium-$VERSION-linux-x64.tar.gz"
        ;;
    
    macos)
        echo "Creating macOS DMG..."
        # The build creates Thomas Chromium.app
        hdiutil create -volname "Thomas Chromium" \
            -srcfolder "$BUILD_DIR/Thomas Chromium.app" \
            -ov -format UDZO \
            "$OUT_DIR/thomas-chromium-$VERSION-macos.dmg"
        echo "Package: $OUT_DIR/thomas-chromium-$VERSION-macos.dmg"
        ;;
    
    *)
        echo "Unknown platform: $PLATFORM"
        exit 1
        ;;
esac

echo "Packaging complete!"
