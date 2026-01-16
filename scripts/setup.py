#!/usr/bin/env python3
"""
Thomas Chromium - Setup Script
Downloads and configures Chromium source with patches.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# Configuration
CHROMIUM_VERSION = "131.0.6778.139"
DEPOT_TOOLS_URL = "https://chromium.googlesource.com/chromium/tools/depot_tools.git"

ROOT_DIR = Path(__file__).parent.parent.absolute()
DEPOT_TOOLS_DIR = ROOT_DIR / "depot_tools"
SRC_DIR = ROOT_DIR / "src"
PATCHES_DIR = ROOT_DIR / "patches"


def run_command(cmd, cwd=None, env=None):
    """Run a command and handle errors."""
    print(f"Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        shell=isinstance(cmd, str),
        capture_output=False
    )
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}")
        sys.exit(1)


def setup_depot_tools():
    """Clone and set up depot_tools."""
    if DEPOT_TOOLS_DIR.exists():
        print("depot_tools already exists, updating...")
        run_command(["git", "pull"], cwd=DEPOT_TOOLS_DIR)
    else:
        print("Cloning depot_tools...")
        run_command(["git", "clone", DEPOT_TOOLS_URL, str(DEPOT_TOOLS_DIR)])
    
    # Add depot_tools to PATH
    os.environ["PATH"] = str(DEPOT_TOOLS_DIR) + os.pathsep + os.environ["PATH"]
    print(f"Added depot_tools to PATH")


def fetch_chromium():
    """Fetch the Chromium source code."""
    if not SRC_DIR.exists():
        SRC_DIR.mkdir(parents=True)
    
    # Create .gclient file
    gclient_content = f"""
solutions = [
  {{
    "name": "src",
    "url": "https://chromium.googlesource.com/chromium/src.git@{CHROMIUM_VERSION}",
    "managed": False,
    "custom_deps": {{}},
    "custom_vars": {{}},
  }},
]
"""
    gclient_file = ROOT_DIR / ".gclient"
    gclient_file.write_text(gclient_content)
    
    print(f"Fetching Chromium {CHROMIUM_VERSION}...")
    run_command("gclient sync --nohooks --no-history", cwd=ROOT_DIR)
    
    print("Running hooks...")
    run_command("gclient runhooks", cwd=ROOT_DIR)


def apply_patches():
    """Apply Thomas Chromium patches."""
    if not PATCHES_DIR.exists():
        print("No patches directory found, skipping...")
        return
    
    series_file = PATCHES_DIR / "series"
    if not series_file.exists():
        print("No patch series file found, skipping...")
        return
    
    print("Applying patches...")
    for patch_name in series_file.read_text().strip().split("\n"):
        patch_name = patch_name.strip()
        if not patch_name or patch_name.startswith("#"):
            continue
        
        patch_file = PATCHES_DIR / patch_name
        if patch_file.exists():
            print(f"Applying: {patch_name}")
            run_command(
                ["git", "apply", "--3way", str(patch_file)],
                cwd=SRC_DIR
            )


def main():
    """Main setup function."""
    platform = sys.argv[1] if len(sys.argv) > 1 else sys.platform
    
    print("=" * 60)
    print(f"Thomas Chromium Setup - {platform}")
    print("=" * 60)
    
    setup_depot_tools()
    fetch_chromium()
    apply_patches()
    
    print("\n" + "=" * 60)
    print("Setup complete! Run 'python scripts/build.py' to build.")
    print("=" * 60)


if __name__ == "__main__":
    main()
