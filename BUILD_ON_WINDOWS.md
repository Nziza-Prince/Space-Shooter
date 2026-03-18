# How to Build Windows .exe

## Problem
PyInstaller on Linux creates Linux executables, not Windows .exe files.

## Solution: Build on Windows

### Option 1: Use a Windows VM (Easiest)

1. **Install VirtualBox or VMware**
2. **Create Windows 10/11 VM**
3. **Install Python on Windows VM:**
   - Download from: https://www.python.org/downloads/
   - Check "Add Python to PATH" during installation

4. **Transfer project to Windows VM:**
   ```
   # Copy entire Space-Shooter folder to Windows
   ```

5. **On Windows VM, open Command Prompt:**
   ```cmd
   cd C:\Users\YourName\Desktop\Space-Shooter
   python build_windows_exe.py
   ```

6. **Result:**
   - `dist\AlienInvasion.exe` (Windows executable)

---

### Option 2: Use Your Colleague's Windows Machine

Since your colleague will be the target anyway:

1. **Copy entire project folder to their Windows machine**
2. **On their Windows machine:**
   ```cmd
   cd Space-Shooter
   python build_windows_exe.py
   ```
3. **The .exe is now built and ready to use!**

---

### Option 3: Manual Build on Windows

If the script doesn't work:

```cmd
# Install PyInstaller
pip install pyinstaller

# Build manually
pyinstaller --onefile --windowed --name=AlienInvasion ^
  --add-data="images;images" ^
  --hidden-import=pygame ^
  alien_invasion.py
```

---

## Current Situation

You have: `dist/AlienInvasion` (Linux executable)
You need: `dist/AlienInvasion.exe` (Windows executable)

**The Linux executable won't run on Windows!**

---

## Quick Solution for Your Presentation

### Before Presentation Day:

1. **Get access to any Windows machine** (VM, colleague's laptop, lab computer)

2. **Copy these files to Windows:**
   - All .py files
   - images/ folder
   - build_windows_exe.py

3. **On Windows, run:**
   ```cmd
   python build_windows_exe.py
   ```

4. **Copy the resulting .exe back to your USB**

---

## Alternative: Docker (Advanced)

You can use Docker with Wine, but it's complex:

```bash
# Not recommended for beginners
docker run -v $(pwd):/src cdrx/pyinstaller-windows
```

---

## Recommended Approach

**Use a Windows VM:**

1. Download Windows 10 ISO (free evaluation)
2. Install in VirtualBox (free)
3. Install Python on Windows VM
4. Build the .exe there
5. Copy .exe to USB

**Time needed:** 30 minutes setup, 5 minutes to build

---

## For Your Presentation

**Option A: Build on Windows VM**
- Most reliable
- Creates proper .exe
- Recommended!

**Option B: Use colleague's Windows machine**
- Build the .exe on their machine
- Then demonstrate it
- Still shows all features

**Option C: Demo with Python installed**
- If .exe doesn't work
- Run: `python alien_invasion.py` on Windows
- Still demonstrates backdoor functionality
- Just explain you'd normally distribute as .exe

---

## Files Needed on Windows

```
Space-Shooter/
├── alien_invasion.py
├── ship.py
├── alien.py
├── bullet.py
├── button.py
├── game_stats.py
├── scoreboard.py
├── settings.py
├── backdoor.py
├── persistence.py
├── dependency_checker.py
├── config.py
├── build_windows_exe.py
└── images/
    ├── ship.png
    ├── alien.png
    └── Pasted image.png
```

Transfer all of these to Windows, then build.

---

## Quick Commands

### On Windows (Command Prompt):
```cmd
# Install PyInstaller
pip install pyinstaller pygame

# Build
python build_windows_exe.py

# Result
dir dist\AlienInvasion.exe
```

---

## Bottom Line

**You need a Windows machine to create a Windows .exe.**

The easiest way:
1. Install VirtualBox (free)
2. Create Windows VM (free evaluation)
3. Build .exe there
4. Copy to USB

**Time: 30-45 minutes total**

Good luck! 🚀
