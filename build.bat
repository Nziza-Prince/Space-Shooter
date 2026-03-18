@echo off
REM Simple Windows build script

echo ==========================================
echo Building Windows Executable
echo ==========================================
echo.

REM Install PyInstaller if needed
echo Checking PyInstaller...
python -m pip install pyinstaller pygame
echo.

REM Build using the spec file
echo Building...
python -m PyInstaller build_windows_simple.spec

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==========================================
    echo BUILD SUCCESSFUL!
    echo ==========================================
    echo.
    echo Your .exe is ready:
    echo   dist\AlienInvasion.exe
    echo.
    echo Files to copy:
    echo   1. dist\AlienInvasion.exe
    echo   2. images\ folder
    echo.
    pause
) else (
    echo.
    echo BUILD FAILED!
    echo.
    pause
)
