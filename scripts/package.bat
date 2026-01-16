@echo off
REM Thomas Chromium - Package Script (Windows)
setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0
set ROOT_DIR=%SCRIPT_DIR%..
set VERSION=1.0.0

echo === Thomas Chromium Package - Windows ===

set BUILD_DIR=%ROOT_DIR%\src\out\Release
set OUT_DIR=%ROOT_DIR%\out

if not exist "%OUT_DIR%" mkdir "%OUT_DIR%"

echo Creating Windows ZIP package...
cd /d "%BUILD_DIR%"

REM Create ZIP with essential files
powershell -Command "Compress-Archive -Path 'chrome.exe','*.dll','*.pak','*.dat','*.bin','locales','resources' -DestinationPath '%OUT_DIR%\thomas-chromium-%VERSION%-windows-x64.zip' -Force"

echo Package: %OUT_DIR%\thomas-chromium-%VERSION%-windows-x64.zip
echo.
echo To create an installer, use NSIS or Inno Setup with the packaged files.

endlocal
