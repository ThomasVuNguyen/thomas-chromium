@echo off
REM Thomas Chromium - Setup Script (Windows)
setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0
set ROOT_DIR=%SCRIPT_DIR%..

echo === Thomas Chromium Setup - Windows ===

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is required
    exit /b 1
)

REM Run Python setup script
python "%SCRIPT_DIR%setup.py" windows

endlocal
