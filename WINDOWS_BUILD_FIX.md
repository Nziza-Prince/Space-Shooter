# Windows Build Fix

## The Error
Your colleague got: `FileNotFoundError: [WinError 2] The system cannot find the file specified`

This means PyInstaller command isn't in PATH.

---

## Quick Fix - 3 Methods

### Method 1: Use the Batch File (Easiest) ⭐

Tell your colleague to run:
```cmd
build.bat
```

That's it! Double-click `build.bat` or run it from command prompt.

---

### Method 2: Use the Simple Python Script

```cmd
python build_windows_simple.py
```

This uses `python -m PyInstaller` instead of just `pyinstaller`, which works better.

---

### Method 3: Use the Spec File Directly

```cmd
python -m pip install pyinstaller pygame
python -m PyInstaller build_windows_simple.spec
```

---

## What Your Colleague Should Do Right Now

1. **Open Command Prompt (not Git Bash)**
   - Press `Win + R`
   - Type `cmd`
   - Press Enter

2. **Navigate to project:**
   ```cmd
   cd C:\Users\hirwa\Space-Shooter
   ```

3. **Run the batch file:**
   ```cmd
   build.bat
   ```

4. **Wait 2-3 minutes**

5. **Check result:**
   ```cmd
   dir dist\AlienInvasion.exe
   ```

---

## Why Git Bash Failed

Git Bash (MINGW64) has issues with Windows paths and commands. Use regular Windows Command Prompt instead.

---

## Alternative: Manual Build

If all else fails:

```cmd
REM Install dependencies
python -m pip install pyinstaller pygame

REM Build manually
python -m PyInstaller --onefile --windowed --name=AlienInvasion --add-data="images;images" alien_invasion.py

REM Check result
dir dist\AlienInvasion.exe
```

---

## Expected Output

When successful:
```
Building Windows Executable
...
Building EXE from EXE-00.toc completed successfully.
...
BUILD SUCCESSFUL!

Your .exe is ready:
  dist\AlienInvasion.exe
```

---

## Files to Copy After Build

```
USB Drive/
├── AlienInvasion.exe  (from dist\ folder)
└── images/
    ├── ship.png
    ├── alien.png
    └── Pasted image.png
```

---

## Quick Commands for Your Colleague

```cmd
REM Use Command Prompt, not Git Bash!
cd C:\Users\hirwa\Space-Shooter
build.bat
```

That's it! 🚀
