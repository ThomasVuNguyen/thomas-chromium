# Local Development Setup

This guide helps you set up a local development environment for fast iteration.

## Prerequisites

- Ubuntu 22.04+ (or similar Linux distro)
- 16GB+ RAM (24GB recommended)
- 100GB+ free disk space
- 8+ CPU cores

## Quick Start

### 1. Install Dependencies

```bash
# Install build deps
sudo apt-get update
sudo apt-get install -y git python3 python3-pip curl wget lsb-release sudo \
    pkg-config file xz-utils build-essential ninja-build clang lld \
    gperf bison flex ruby ccache \
    libgtk-3-dev libglib2.0-dev libnss3-dev libcups2-dev libxss-dev \
    libasound2-dev libxkbcommon-dev libdrm-dev libgbm-dev

# Configure ccache (optional but recommended)
ccache --set-config=max_size=20G
ccache --set-config=compression=true
```

### 2. Get depot_tools

```bash
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git ~/depot_tools
echo 'export PATH="$HOME/depot_tools:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 3. Fetch Chromium (First time only - takes 1-2 hours)

```bash
mkdir -p ~/chromium && cd ~/chromium
fetch --nohooks --no-history chromium
cd src
git fetch --tags
git checkout 131.0.6778.139
gclient sync --nohooks -D
./build/install-build-deps.sh
gclient runhooks
```

### 4. Create Development Build Config

```bash
cd ~/chromium/src
mkdir -p out/Debug

cat > out/Debug/args.gn << 'EOF'
# Fast development build
is_debug = true
is_component_build = true    # Key for fast rebuilds!
symbol_level = 1
enable_nacl = false
cc_wrapper = "ccache"        # Cache compilations
use_sysroot = true

# Optional: enable these for debugging
# dcheck_always_on = true
# is_asan = true
EOF

# Generate build files
gn gen out/Debug
```

### 5. Build (First time: 2-4 hours, subsequent: minutes)

```bash
cd ~/chromium/src
ninja -C out/Debug chrome -j$(nproc)
```

### 6. Run Your Browser

```bash
./out/Debug/chrome
```

## Development Workflow

### Making Changes

1. Edit source files in `src/`
2. Rebuild (only changed files compile):
   ```bash
   ninja -C out/Debug chrome
   ```
3. Run and test:
   ```bash
   ./out/Debug/chrome
   ```

### Typical Rebuild Times

| Change Type | Time |
|-------------|------|
| One .cc file | 30 sec - 2 min |
| One header file | 5-15 min |
| Web UI (HTML/CSS/JS) | Instant (no rebuild) |
| Build system changes | 10-30 min |

## Tips

### Speed Up Builds
- Use `component_build = true` (already set above)
- Use ccache (already set above)
- Close unnecessary applications to free RAM
- Use `-j$(nproc)` to use all CPU cores

### Debug Build vs Release Build
- **out/Debug** - Fast rebuilds, slow runtime (for development)
- **out/Release** - Slow rebuilds, fast runtime (for distribution)

### Apply Patches
```bash
cd ~/chromium/src
git apply /path/to/your/patch.patch
```

### Check for Errors
```bash
# Syntax check without building
gn gen out/Debug --check

# Run Chromium tests
./out/Debug/unit_tests
```

## Troubleshooting

### "gn: command not found"
Make sure depot_tools is in your PATH:
```bash
export PATH="$HOME/depot_tools:$PATH"
```

### Out of memory during build
Reduce parallel jobs:
```bash
ninja -C out/Debug chrome -j4  # Use 4 instead of all cores
```

### ccache not working
Check ccache stats:
```bash
ccache -s
```

## Directory Structure

```
~/chromium/
└── src/
    ├── chrome/          # Main browser code
    ├── content/         # Core engine
    ├── out/
    │   ├── Debug/       # Your dev build
    │   └── Release/     # Release build (CI)
    └── ...
```
