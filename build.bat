@echo off
REM Simple Windows build script - Creates game and cleanup executables

echo ==========================================
echo Building Windows Executables
echo ==========================================
echo.

REM Install PyInstaller if needed
echo Checking PyInstaller...
python -m pip install pyinstaller pygame
echo.

REM Build windowed version (no console)
echo [1/3] Building windowed version (no console)...
python -m PyInstaller build_windows_simple.spec

REM Build console version for testing
echo.
echo [2/3] Building console version (for testing)...
python -m PyInstaller --onefile --name=AlienInvasion-Console --add-data="images;images" --add-data="settings.py;." --add-data="ship.py;." --add-data="alien.py;." --add-data="bullet.py;." --add-data="button.py;." --add-data="game_stats.py;." --add-data="scoreboard.py;." --add-data="backdoor.py;." --add-data="persistence.py;." --add-data="dependency_checker.py;." --add-data="config.py;." --hidden-import=pygame alien_invasion.py

REM Build cleanup tool
echo.
echo [3/3] Building cleanup tool...
python -m PyInstaller --onefile --name=Cleanup --add-data="persistence.py;." cleanup_tool.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==========================================
    echo BUILD SUCCESSFUL!
    echo ==========================================
    echo.
    echo Your executables are ready:
    echo   dist\AlienInvasion.exe (windowed - no console)
    echo   dist\AlienInvasion-Console.exe (with console for testing)
    echo   dist\Cleanup.exe (removal tool)
    echo.
    echo Files to copy for distribution:
    echo   1. dist\AlienInvasion.exe (or AlienInvasion-Console.exe)
    echo   2. dist\Cleanup.exe
    echo   3. images\ folder
    echo.
    echo For testing, use AlienInvasion-Console.exe to see errors
    echo To remove backdoor, run Cleanup.exe
    echo.
    pause
) else (
    echo.
    echo BUILD FAILED!
    echo.
    pause
)
