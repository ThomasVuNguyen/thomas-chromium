# Thomas Chromium

[![Build Status](https://api.cirrus-ci.com/github/ThomasVuNguyen/thomas-chromium.svg)](https://cirrus-ci.com/github/ThomasVuNguyen/thomas-chromium)

## Features

- 🛡️ Built-in ad blocking
- 🔒 Enhanced privacy (tracker protection)
- 🎨 Customizable UI
- 🧩 Full Chrome extension support
- 🖥️ Cross-platform (Windows, macOS, Linux)

## Building

Builds are automated via [Cirrus CI](https://cirrus-ci.com/) for all platforms.

### Prerequisites (Local Development)

- Python 3.9+
- Git
- 100GB+ free disk space
- 16GB+ RAM

### Quick Start

```bash
# Clone the repository
git clone https://github.com/user/thomas-chromium.git
cd thomas-chromium

# Set up the build environment
python scripts/setup.py

# Apply patches and build
python scripts/build.py
```

## Project Structure

```
thomas-chromium/
├── .cirrus.yml          # CI/CD configuration
├── patches/             # Custom Chromium patches
├── scripts/             # Build and utility scripts
├── branding/            # Icons, logos, assets
└── config/              # Build configuration
```

## Downloads

See [Releases](https://github.com/user/thomas-chromium/releases) for pre-built binaries.

## License

BSD 3-Clause (same as Chromium)
