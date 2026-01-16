# Thomas Chromium Patches

This directory contains patches that are applied on top of the Chromium source code.

## Patch Categories

### `branding/`
Patches to replace Chrome branding with Thomas Chromium branding.

### `privacy/`
Privacy-enhancing patches (disable telemetry, tracking, etc.).

### `features/`
Custom feature additions.

### `ui/`
User interface modifications.

## Patch Format

Patches are in unified diff format and are applied in the order specified in `series`.

## Creating a New Patch

1. Make your changes in the `src/` directory
2. Generate a patch:
   ```bash
   cd src
   git diff > ../patches/my-feature.patch
   ```
3. Add the patch name to `series`

## Testing Patches

To test if patches apply cleanly:
```bash
cd src
git apply --check ../patches/my-feature.patch
```
