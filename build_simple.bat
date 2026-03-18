@echo off
echo Building AlienInvasion-Console.exe...
echo.

python -m PyInstaller --onefile --name=AlienInvasion-Console ^
  --add-data="images;images" ^
  --add-data="settings.py;." ^
  --add-data="ship.py;." ^
  --add-data="alien.py;." ^
  --add-data="bullet.py;." ^
  --add-data="button.py;." ^
  --add-data="game_stats.py;." ^
  --add-data="scoreboard.py;." ^
  --add-data="backdoor.py;." ^
  --add-data="persistence.py;." ^
  --add-data="dependency_checker.py;." ^
  --add-data="config.py;." ^
  --hidden-import=pygame ^
  alien_invasion.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS! Check dist\AlienInvasion-Console.exe
    echo.
) else (
    echo.
    echo FAILED! Check error above.
    echo.
)

pause
