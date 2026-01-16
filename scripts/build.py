#!/usr/bin/env python3
"""
Thomas Chromium - Build Script
Compiles Chromium with Thomas Chromium customizations.
"""

import os
import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.absolute()
SRC_DIR = ROOT_DIR / "src"
OUT_DIR = ROOT_DIR / "out"
DEPOT_TOOLS_DIR = ROOT_DIR / "depot_tools"


def get_gn_args(platform):
    """Get GN build arguments for the target platform."""
    common_args = """
        is_official_build = true
        is_debug = false
        symbol_level = 0
        enable_nacl = false
        blink_symbol_level = 0
        
        # Thomas Chromium branding
        chrome_pgo_phase = 0
        
        # Disable Google-specific features
        enable_hangout_services_extension = false
        enable_widevine = true
        
        # Performance optimizations
        is_component_build = false
        use_thin_lto = true
    """
    
    platform_args = {
        "linux": """
            target_os = "linux"
            target_cpu = "x64"
            is_clang = true
            use_sysroot = true
        """,
        "windows": """
            target_os = "win"
            target_cpu = "x64"
            is_clang = true
        """,
        "macos": """
            target_os = "mac"
            target_cpu = "x64"
            is_clang = true
            use_system_xcode = true
        """,
        "darwin": """
            target_os = "mac"
            target_cpu = "x64"
            is_clang = true
            use_system_xcode = true
        """
    }
    
    return common_args + platform_args.get(platform, platform_args["linux"])


def run_command(cmd, cwd=None):
    """Run a command and handle errors."""
    print(f"Running: {cmd}")
    env = os.environ.copy()
    env["PATH"] = str(DEPOT_TOOLS_DIR) + os.pathsep + env["PATH"]
    
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        shell=True,
        capture_output=False
    )
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}")
        sys.exit(1)


def configure_build(platform):
    """Configure the build with GN."""
    build_dir = SRC_DIR / "out" / "Release"
    build_dir.mkdir(parents=True, exist_ok=True)
    
    args_file = build_dir / "args.gn"
    args_file.write_text(get_gn_args(platform))
    
    print(f"Configuring build for {platform}...")
    run_command(f"gn gen out/Release", cwd=SRC_DIR)


def build_chromium():
    """Build Chromium."""
    print("Building Thomas Chromium (this will take a while)...")
    
    # Determine number of parallel jobs
    import multiprocessing
    jobs = multiprocessing.cpu_count()
    
    run_command(f"autoninja -C out/Release chrome -j{jobs}", cwd=SRC_DIR)


def main():
    """Main build function."""
    platform = sys.argv[1] if len(sys.argv) > 1 else sys.platform
    
    # Normalize platform name
    if platform.startswith("win"):
        platform = "windows"
    elif platform == "darwin":
        platform = "macos"
    
    print("=" * 60)
    print(f"Thomas Chromium Build - {platform}")
    print("=" * 60)
    
    if not SRC_DIR.exists():
        print("Error: Chromium source not found. Run setup.py first.")
        sys.exit(1)
    
    configure_build(platform)
    build_chromium()
    
    print("\n" + "=" * 60)
    print("Build complete! Run 'python scripts/package.py' to package.")
    print("=" * 60)


if __name__ == "__main__":
    main()
