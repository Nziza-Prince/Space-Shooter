@echo off
REM Build only the cleanup tool

echo ==========================================
echo Building Cleanup Tool
echo ==========================================
echo.

python -m PyInstaller --onefile --name=Cleanup --add-data="persistence.py;." cleanup_tool.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==========================================
    echo BUILD SUCCESSFUL!
    echo ==========================================
    echo.
    echo Cleanup.exe is ready:
    echo   dist\Cleanup.exe
    echo.
) else (
    echo.
    echo BUILD FAILED!
    echo Check the error above.
    echo.
)

pause
