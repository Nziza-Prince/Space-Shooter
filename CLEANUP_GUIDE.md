# Cleanup Tool Guide

## Overview

The Cleanup Tool (`Cleanup.exe`) completely removes all traces of the backdoor from the system.

---

## What It Removes

1. ✅ **Running Backdoor Processes**
   - Kills any active backdoor connections
   - Terminates game processes
   - Stops background Python processes

2. ✅ **Persistence Mechanisms**
   - Windows: Registry Run keys
   - Linux: Autostart .desktop files
   - Linux: Cron jobs

3. ✅ **Temporary Files**
   - Backdoor script files in temp directory
   - Any leftover configuration files

4. ✅ **Verification**
   - Checks that everything was removed
   - Reports any remaining issues

---

## How to Use

### On Windows:

**Method 1: Double-click**
1. Double-click `Cleanup.exe`
2. Read the warning
3. Type `yes` and press Enter
4. Wait for cleanup to complete

**Method 2: Command Prompt**
```cmd
cd C:\Users\YourName\Desktop\AlienInvasion
Cleanup.exe
```

### On Linux:

```bash
python3 cleanup_tool.py
```

---

## What You'll See

```
============================================================
ALIEN INVASION - CLEANUP TOOL
============================================================

This tool will remove all traces of the backdoor:
  • Kill running backdoor processes
  • Remove persistence mechanisms (autostart)
  • Remove temporary files
  • Clean up registry entries (Windows)

Do you want to proceed? (yes/no): yes

============================================================
CLEANING UP...
============================================================

[1/4] Killing backdoor processes...
  ✓ Backdoor processes terminated

[2/4] Removing persistence mechanisms...
  ✓ Persistence mechanisms removed

[3/4] Removing temporary files...
  ✓ Removed 2 temporary file(s)

[4/4] Verifying cleanup...
  ✓ System is clean

============================================================
CLEANUP COMPLETE!
============================================================

✓ All backdoor components have been removed!
✓ Your system is clean

The game folder can now be safely deleted.

============================================================
Press Enter to exit...
```

---

## After Cleanup

### What's Removed:
- ✅ Backdoor no longer runs
- ✅ Game won't auto-start on boot
- ✅ No background processes
- ✅ No registry entries
- ✅ No scheduled tasks

### What Remains:
- The game folder (can be manually deleted)
- The .exe files (can be manually deleted)
- The images folder (can be manually deleted)

### To Completely Remove:
1. Run `Cleanup.exe`
2. Delete the entire game folder
3. Empty Recycle Bin

---

## Verification

### Check if Backdoor is Running:

**Windows:**
```cmd
tasklist | findstr python
tasklist | findstr AlienInvasion
```

**Linux:**
```bash
ps aux | grep alien_invasion
ps aux | grep backdoor
```

### Check Persistence:

**Windows:**
```cmd
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
```

**Linux:**
```bash
ls ~/.config/autostart/
crontab -l
```

---

## Manual Cleanup (If Tool Fails)

### Windows:

1. **Kill Processes:**
   - Open Task Manager (Ctrl+Shift+Esc)
   - Find and end: `python.exe`, `pythonw.exe`, `AlienInvasion.exe`

2. **Remove Registry:**
   - Press Win+R, type `regedit`
   - Navigate to: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
   - Delete `AlienInvasion` entry

3. **Remove Files:**
   - Delete game folder
   - Check `%TEMP%` for backdoor files

### Linux:

1. **Kill Processes:**
   ```bash
   pkill -f alien_invasion
   pkill -f backdoor
   ```

2. **Remove Autostart:**
   ```bash
   rm ~/.config/autostart/alien_invasion.desktop
   ```

3. **Remove Cron:**
   ```bash
   crontab -e
   # Delete lines containing "alien_invasion"
   ```

4. **Remove Files:**
   ```bash
   rm -rf ~/path/to/Space-Shooter
   ```

---

## For Presentation

### Demonstrate Cleanup:

1. **Show backdoor is running:**
   - Task Manager shows processes
   - Listener has active connection

2. **Run Cleanup.exe:**
   - Show the cleanup process
   - Show each step completing

3. **Verify removal:**
   - Check Task Manager - no processes
   - Check Registry - no entries
   - Check listener - connection closed

4. **Explain what was removed:**
   - Persistence mechanisms
   - Running processes
   - Temporary files

---

## Troubleshooting

### "Access Denied" Error

**Cause:** Process is running with higher privileges

**Solution:**
1. Close all game windows
2. Run Cleanup.exe as Administrator
   - Right-click → Run as administrator

### "Some mechanisms remain"

**Cause:** Files are locked or in use

**Solution:**
1. Restart computer
2. Run Cleanup.exe again
3. Or follow manual cleanup steps

### Cleanup.exe Won't Run

**Cause:** Antivirus blocking it

**Solution:**
1. Temporarily disable antivirus
2. Or use: `python cleanup_tool.py`

---

## Files Included

When distributing the game, include:

```
Distribution Package/
├── AlienInvasion.exe (or AlienInvasion-Console.exe)
├── Cleanup.exe
└── images/
    ├── ship.png
    ├── alien.png
    └── Pasted image.png
```

---

## Assignment Requirement

This cleanup tool fulfills the requirement:

> "Make another app that will remove everything added to start-up programs by your app."

✅ Removes startup programs  
✅ Kills running processes  
✅ Removes temporary files  
✅ Verifies cleanup  
✅ Provides manual instructions if needed  

---

## Safety Note

The cleanup tool is safe to run multiple times. It will:
- Not harm your system
- Only remove backdoor-related items
- Provide clear feedback
- Offer manual steps if automatic cleanup fails

---

## Summary

**To remove the backdoor:**
1. Run `Cleanup.exe`
2. Type `yes`
3. Wait for completion
4. Delete game folder

**That's it!** Your system is clean. 🧹✨
