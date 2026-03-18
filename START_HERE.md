# 🚀 START HERE - Complete Setup in 3 Steps

## Your Scenario
- **You:** Kali Linux (attacker/listener)
- **Colleague:** Windows (target/gamer)
- **Goal:** Give colleague a game → Get their shell access

---

## 🎯 Quick Setup (3 Steps)

### Step 1: Build the Windows .exe (5 minutes)

On your Kali Linux:

```bash
cd ~/Documents/Space-Shooter
./quick_build.sh
```

This will:
- ✅ Get your Kali IP automatically
- ✅ Update config.py
- ✅ Install PyInstaller if needed
- ✅ Build AlienInvasion.exe

**Output:** `dist/AlienInvasion.exe`

---

### Step 2: Prepare USB for Colleague (2 minutes)

Copy to USB drive:
```
USB/
├── AlienInvasion.exe  (from dist/ folder)
└── images/
    ├── ship.png
    ├── alien.png
    └── Pasted image.png
```

Give USB to your colleague.

---

### Step 3: Run the Demo (5 minutes)

#### On Your Kali (You):
```bash
python3 listener.py
```
Wait for connection...

#### On Windows (Colleague):
1. Copy files from USB to Desktop
2. Double-click `AlienInvasion.exe`
3. Type `YES` in consent dialog
4. Play the game!

#### Back on Your Kali (You):
```bash
shell> whoami
shell> hostname
shell> dir
shell> ipconfig
```

**You now have shell access!** ✅

---

## 📚 Documentation Files

Choose based on what you need:

| File | Purpose | When to Use |
|------|---------|-------------|
| **SIMPLE_GUIDE.md** | Step-by-step for your exact scenario | Read this first! |
| **WINDOWS_BUILD_GUIDE.md** | Detailed .exe building instructions | If build fails |
| **KALI_SETUP.md** | Kali Linux specific setup | Troubleshooting Kali |
| **DOCUMENTATION.md** | Complete technical documentation | For assignment report |
| **REQUIREMENTS_CHECKLIST.md** | Verify all 50 points covered | Before submission |

---

## ⚡ Super Quick Reference

### Build:
```bash
./quick_build.sh
```

### Start Listener:
```bash
python3 listener.py
```

### Files to Give Colleague:
- `dist/AlienInvasion.exe`
- `images/` folder

### Commands to Try:
```bash
whoami
hostname
dir
ipconfig
tasklist
systeminfo
```

---

## ✅ Pre-Presentation Checklist

**Day Before:**
- [ ] Run `./quick_build.sh`
- [ ] Test on Windows VM
- [ ] Verify connection works
- [ ] Test persistence (restart Windows)
- [ ] Test cleanup tool

**Presentation Day:**
- [ ] Both laptops charged
- [ ] Both on same WiFi
- [ ] USB with files ready
- [ ] Backup video/screenshots ready

---

## 🆘 Quick Troubleshooting

### No Connection?
```bash
# Check you're on same network
ping COLLEAGUE_IP

# Allow firewall
sudo ufw allow 4444
```

### Windows Defender Blocks?
- Add folder exclusion in Windows Security
- Or disable Real-time protection temporarily

### Game Won't Start?
- Check `images/` folder is present
- All 3 images must be there

---

## 🎓 Assignment Requirements (50 Points)

All requirements are met:

| Requirement | Points | Status |
|-------------|--------|--------|
| User notification | 5 | ✅ Consent dialog |
| Dependencies installed | 5 | ✅ Auto-installer |
| Uninterrupted gameplay | 10 | ✅ Background thread |
| Shell access | 10 | ✅ Reverse shell |
| Persistence | 5 | ✅ Auto-start |
| Cleanup tool | 5 | ✅ cleanup_tool.py |
| Documentation | 5 | ✅ Complete docs |
| Innovation | 5 | ✅ Consent + cross-platform |
| **TOTAL** | **50** | **✅** |

---

## 🎬 Presentation Flow (10 minutes)

1. **Intro** (1 min): Explain the concept
2. **Show Kali** (1 min): Start listener
3. **Show Windows** (1 min): Run game
4. **Show Access** (2 min): Execute commands
5. **Show Persistence** (2 min): Restart Windows
6. **Show Cleanup** (1 min): Remove persistence
7. **Explain Defenses** (2 min): Detection & prevention

---

## 📞 Need Help?

1. Read `SIMPLE_GUIDE.md` - Most common issues covered
2. Check `WINDOWS_BUILD_GUIDE.md` - Build problems
3. Review `DOCUMENTATION.md` - Technical details

---

## 🎯 The Bottom Line

```bash
# You (Kali)
./quick_build.sh          # Build .exe
python3 listener.py       # Start listening

# Colleague (Windows)
# Double-click AlienInvasion.exe

# You (Kali)
# You now have their shell! 🎉
```

**That's it! Good luck on March 18! 🚀**
