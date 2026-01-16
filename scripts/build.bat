@echo off
REM Thomas Chromium - Build Script (Windows)
setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0
set ROOT_DIR=%SCRIPT_DIR%..

echo === Thomas Chromium Build - Windows ===

python "%SCRIPT_DIR%build.py" windows

endlocal
