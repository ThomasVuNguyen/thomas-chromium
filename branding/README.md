# Thomas Chromium - Branding Assets

This directory contains branding assets for Thomas Chromium.

## Required Assets

### Icons (replace with your designs)

| File | Size | Purpose |
|------|------|---------|
| `icon_16.png` | 16x16 | Favicon, small icons |
| `icon_32.png` | 32x32 | Taskbar (Windows) |
| `icon_48.png` | 48x48 | App list icons |
| `icon_128.png` | 128x128 | Web Store, large icons |
| `icon_256.png` | 256x256 | High-DPI icons |
| `app.icns` | Multi-size | macOS app icon |
| `app.ico` | Multi-size | Windows app icon |

### Other Assets

- `product_logo.svg` - Vector logo for web/print
- `splash.png` - Loading/splash screen (optional)

## Generating Icons

Use a tool like ImageMagick to generate all sizes from a master file:

```bash
# From a 512x512 master icon
convert master.png -resize 16x16 icon_16.png
convert master.png -resize 32x32 icon_32.png
convert master.png -resize 48x48 icon_48.png
convert master.png -resize 128x128 icon_128.png
convert master.png -resize 256x256 icon_256.png
```

## Updating Branding in Chromium

The branding patches in `/patches/branding/` reference these assets.
