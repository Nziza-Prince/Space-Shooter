# Presentation Guide - March 18, 2026

## 📋 Pre-Presentation Checklist

### One Week Before:
- [ ] Test full setup in VMs
- [ ] Build Windows .exe
- [ ] Verify all features work
- [ ] Practice demo flow
- [ ] Prepare backup plans

### Day Before:
- [ ] Charge laptop
- [ ] Test VMs boot properly
- [ ] Verify network connectivity
- [ ] Print documentation (backup)
- [ ] Prepare presentation slides (optional)

### Day Of (Before 13:30):
- [ ] Boot both VMs
- [ ] Verify network connectivity
- [ ] Start listener on Kali
- [ ] Test connection once
- [ ] Have cleanup tool ready

---

## 🎯 Presentation Structure (Recommended)

### 1. Introduction (2 minutes)

**What to say:**
> "We've created an educational backdoor demonstration disguised as a game. This shows how malware can hide in legitimate-looking software and demonstrates important cybersecurity concepts."

**Show:**
- Team members
- Project overview
- Educational disclaimer

### 2. Architecture Overview (3 minutes)

**What to explain:**
- Target machine (Windows user)
- Attacker machine (Kali Linux)
- How they communicate (reverse shell)
- Why it's stealthy (background thread)

**Show diagram:**
```
Windows Target → Game (Frontend)
                 ↓
                 Backdoor (Background) → Kali Listener
                 ↓
                 Persistence (Autostart)
```

### 3. Live Demonstration (10 minutes)

#### Part A: Initial Setup (2 min)
1. **Show Kali Linux:**
   ```bash
   ip addr show  # Show your IP
   python3 listener.py  # Start listener
   ```
   
2. **Show Windows VM:**
   - Clean desktop
   - Just the game folder
   - No Python installed

#### Part B: Game Execution (3 min)
1. **Run AlienInvasion.exe**
2. **Show consent dialog:**
   - Point out transparency
   - User knows what's happening
   - Educational purpose clear
3. **Accept and start game**
4. **Play briefly** (30 seconds)
   - Show it's a real, working game
   - No visible backdoor activity

#### Part C: Shell Access (3 min)
1. **Switch to Kali:**
   - Show connection received
   - Explain reverse shell concept
   
2. **Execute commands:**
   ```bash
   shell> whoami
   shell> hostname
   shell> dir C:\Users
   shell> systeminfo
   shell> tasklist
   ```
   
3. **Explain what's happening:**
   - Remote command execution
   - Full system access
   - User has no idea

#### Part D: Persistence (2 min)
1. **Restart Windows VM**
2. **Show game auto-starts**
3. **Show connection re-established**
4. **Explain persistence mechanism:**
   - Registry key (Windows)
   - Survives reboot
   - Maintains access

### 4. Features Walkthrough (5 minutes)

#### Requirement 1: Dependency Checking ✅
**Show code:**
```python
# dependency_checker.py
checker = DependencyChecker()
checker.ensure_dependencies()
```

**Explain:**
- Checks for pygame
- Auto-installs if missing
- User sees progress

#### Requirement 2: Shell Access ✅
**Show code:**
```python
# backdoor.py
def execute_command(self, command):
    output = subprocess.check_output(command, shell=True)
    ret