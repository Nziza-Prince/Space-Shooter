@echo off
REM Simple Windows build script - Creates both console and windowed versions

echo ==========================================
echo Building Windows Executable
echo ==========================================
echo.

REM Install PyInstaller if needed
echo Checking PyInstaller...
python -m pip install pyinstaller pygame
echo.

REM Build windowed version (no console)
echo Building windowed version (no console)...
python -m PyInstaller build_windows_simple.spec

REM Build console version for testing
echo.
echo Building console version (for testing)...
python -m PyInstaller --onefile --name=AlienInvasion-Console --add-data="images;images" --add-data="settings.py;." --add-data="ship.py;." --add-data="alien.py;." --add-data="bullet.py;." --add-data="button.py;." --add-data="game_stats.py;." --add-data="scoreboard.py;." --add-data="backdoor.py;." --add-data="persistence.py;." --add-data="dependency_checker.py;." --add-data="config.py;." --hidden-import=pygame alien_invasion.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==========================================
    echo BUILD SUCCESSFUL!
    echo ==========================================
    echo.
    echo Your executables are ready:
    echo   dist\AlienInvasion.exe (windowed - no console)
    echo   dist\AlienInvasion-Console.exe (with console for testing)
    echo.
    echo Files to copy for distribution:
    echo   1. dist\AlienInvasion.exe
    echo   2. images\ folder
    echo.
    echo For testing, use AlienInvasion-Console.exe to see errors
    echo.
    pause
) else (
    echo.
    echo BUILD FAILED!
    echo.
    pause
)
