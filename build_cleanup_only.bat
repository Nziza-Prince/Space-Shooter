@echo off
echo Building Cleanup.exe...
echo.

python -m PyInstaller --onefile --name=Cleanup --add-data="persistence.py;." cleanup_tool.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS! Check dist\Cleanup.exe
    echo.
) else (
    echo.
    echo FAILED! Check error above.
    echo.
)

pause
