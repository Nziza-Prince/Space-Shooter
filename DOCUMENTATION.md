# Alien Invasion - Educational Backdoor Documentation

## ⚠️ DISCLAIMER
This project is for **EDUCATIONAL PURPOSES ONLY** as part of a cybersecurity course assignment. All testing must be conducted in isolated virtual machines. Unauthorized use of this software on systems you don't own is illegal.

---

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Installation & Setup](#installation--setup)
4. [How It Works](#how-it-works)
5. [Testing Instructions](#testing-instructions)
6. [Security Features Demonstrated](#security-features-demonstrated)
7. [Cleanup & Removal](#cleanup--removal)
8. [Ethical Considerations](#ethical-considerations)

---

## Overview

This project demonstrates a backdoor implementation disguised as a legitimate game application. It fulfills the assignment requirements by implementing:

✓ Dependency checking and installation  
✓ Reverse shell access to target system  
✓ Persistence mechanisms (survives reboot)  
✓ Uninterrupted gameplay experience  
✓ Cleanup tool for removal  
✓ User consent and transparency  

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    TARGET MACHINE                        │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │         Alien Invasion Game (Frontend)           │  │
│  │              - Pygame Interface                  │  │
│  │              - Normal Gameplay                   │  │
│  └──────────────────┬───────────────────────────────┘  │
│                     │                                   │
│  ┌──────────────────▼───────────────────────────────┐  │
│  │         Backdoor Module (Background)             │  │
│  │              - Reverse Shell                     │  │
│  │              - Command Execution                 │  │
│  │              - Runs in Daemon Thread             │  │
│  └──────────────────┬───────────────────────────────┘  │
│                     │                                   │
│  ┌──────────────────▼───────────────────────────────┐  │
│  │         Persistence Manager                      │  │
│  │              - Autostart (Linux/Windows)         │  │
│  │              - Registry/Cron                     │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │
                      │ TCP Connection
                      │ (Port 4444)
                      │
┌─────────────────────▼───────────────────────────────────┐
│                  ATTACKER MACHINE                        │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │              Listener (listener.py)              │  │
│  │              - Receives Connection               │  │
│  │              - Sends Commands                    │  │
│  │              - Receives Output                   │  │
│  └──────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

---

## Installation & Setup

### Prerequisites
- Python 3.7+
- Virtual Machine (VMware, VirtualBox, etc.)
- Two VMs or one VM + host machine for testing

### Target Machine Setup

1. Clone or copy the game to the target VM:
```bash
cd ~/Documents
git clone <repository-url> Space-Shooter
cd Space-Shooter
```

2. Configure the listener IP in `config.py`:
```python
LISTENER_HOST = '192.168.1.100'  # Replace with attacker's IP
LISTENER_PORT = 4444
```

3. The game will auto-install dependencies on first run.

### Attacker Machine Setup

1. Ensure Python 3 is installed
2. Navigate to the game directory
3. No additional setup required

---

## How It Works

### 1. Dependency Checking (`dependency_checker.py`)

When the game starts, it checks for required packages:
- Scans for pygame installation
- Automatically installs missing packages using pip
- Provides user feedback during installation

```python
checker = DependencyChecker()
checker.ensure_dependencies()
```

### 2. User Consent (`config.py`)

Before execution, the user sees a consent dialog explaining:
- What the software does
- What permissions it requires
- Educational purpose disclaimer

This ensures transparency and ethical practice.

### 3. Backdoor Connection (`backdoor.py`)

The backdoor module:
- Runs in a background daemon thread
- Connects to the listener via TCP socket
- Executes shell commands received from attacker
- Returns command output
- Fails silently if connection fails (doesn't interrupt game)

**Key Features:**
- Non-blocking: Game runs normally regardless of connection status
- Retry mechanism: Attempts connection 5 times with delays
- Timeout protection: Commands timeout after 30 seconds
- Error handling: Graceful failure without crashing game

### 4. Persistence Mechanism (`persistence.py`)

**Linux Implementation:**
- Creates `.desktop` file in `~/.config/autostart/`
- Adds cron job with `@reboot` trigger
- Dual-method approach for reliability

**Windows Implementation:**
- Adds registry key to `HKEY_CURRENT_USER\...\Run`
- Executes on user login

### 5. Game Execution

The game runs normally with full functionality:
- All controls work as expected
- Graphics render properly
- No visible indication of backdoor
- Performance unaffected

### 6. Listener (`listener.py`)

The attacker runs the listener to receive connections:
```bash
python3 listener.py 4444
```

Features:
- Interactive shell interface
- Command history
- Help system
- Clean exit handling

---

## Testing Instructions

### Step 1: Setup Network

Ensure both VMs can communicate:
```bash
# On target VM
ip addr show

# On attacker VM
ping <target-ip>
```

### Step 2: Start Listener (Attacker Machine)

```bash
cd Space-Shooter
python3 listener.py
```

Expected output:
```
[*] Listener started on 0.0.0.0:4444
[*] Waiting for connection...
```

### Step 3: Run Game (Target Machine)

```bash
cd Space-Shooter
python3 alien_invasion.py
```

The game will:
1. Check dependencies (install if needed)
2. Show consent dialog
3. Start game
4. Connect to listener in background

### Step 4: Verify Connection

On attacker machine, you should see:
```
[+] Connection received from 192.168.1.50:xxxxx
[*] Shell access established.

shell>
```

### Step 5: Test Commands

Try various commands:
```bash
shell> whoami
shell> pwd
shell> ls -la
shell> cat /etc/passwd
shell> ps aux
```

### Step 6: Test Persistence

1. Restart the target VM
2. Listener should receive new connection automatically
3. Verify with: `ps aux | grep python`

### Step 7: Test Cleanup

On target machine:
```bash
python3 cleanup_tool.py
```

Verify persistence removed:
```bash
ls ~/.config/autostart/
crontab -l
```

---

## Security Features Demonstrated

### 1. Dependency Management
- Automatic installation of required packages
- Simulates trojanized software distribution
- Shows how malware can self-install dependencies

### 2. Reverse Shell
- Target initiates connection (bypasses firewalls)
- Encrypted communication possible (not implemented for simplicity)
- Remote command execution

### 3. Persistence
- Multiple methods for reliability
- OS-specific implementations
- Survives reboots and user logouts

### 4. Stealth Techniques
- Background thread execution
- Silent failure (no error messages)
- Legitimate-looking process name
- No console window (when compiled)

### 5. Social Engineering
- Disguised as entertainment software
- User willingly executes the program
- Consent dialog provides false sense of security

---

## Cleanup & Removal

### Automated Cleanup

Run the cleanup tool:
```bash
python3 cleanup_tool.py
```

This removes:
- Autostart entries
- Cron jobs
- Registry keys (Windows)

### Manual Cleanup

**Linux:**
```bash
# Remove autostart
rm ~/.config/autostart/alien_invasion.desktop

# Remove cron job
crontab -e
# Delete lines containing "alien_invasion"

# Kill running process
pkill -f alien_invasion.py
```

**Windows:**
```cmd
# Remove registry entry
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v AlienInvasion /f

# Kill process
taskkill /F /IM python.exe
```

---

## Ethical Considerations

### Legal Compliance
- Only use in controlled environments
- Never deploy on systems without explicit permission
- Understand local cybersecurity laws

### Educational Value
This project demonstrates:
- How backdoors work
- Persistence mechanisms
- Social engineering tactics
- Importance of software verification
- Need for security awareness

### Defense Strategies

**How to detect this type of attack:**
1. Monitor network connections: `netstat -an`
2. Check startup programs: `systemctl list-unit-files --type=service`
3. Review cron jobs: `crontab -l`
4. Use antivirus software
5. Implement application whitelisting
6. Monitor process execution

**Prevention:**
1. Only run software from trusted sources
2. Verify checksums/signatures
3. Use sandboxing for untrusted applications
4. Keep systems updated
5. Implement least privilege principle
6. Use network segmentation

---

## Assignment Checklist

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| Dependency checking | ✅ | `dependency_checker.py` |
| Auto-install dependencies | ✅ | pip subprocess calls |
| Shell access to target | ✅ | `backdoor.py` + `listener.py` |
| Persistence mechanism | ✅ | `persistence.py` (autostart/cron/registry) |
| Uninterrupted gameplay | ✅ | Background daemon thread |
| Cleanup tool | ✅ | `cleanup_tool.py` |
| Documentation | ✅ | This file |

---

## File Structure

```
Space-Shooter/
├── alien_invasion.py      # Main game file (modified)
├── backdoor.py            # Backdoor implementation
├── persistence.py         # Persistence manager
├── listener.py            # Attacker's listener
├── dependency_checker.py  # Dependency management
├── cleanup_tool.py        # Removal tool
├── config.py              # Configuration settings
├── DOCUMENTATION.md       # This file
├── README.md              # User-facing readme
├── ship.py                # Game components
├── alien.py               # Game components
├── bullet.py              # Game components
├── button.py              # Game components
├── game_stats.py          # Game components
├── scoreboard.py          # Game components
├── settings.py            # Game settings
└── images/                # Game assets
    ├── ship.png
    ├── alien.png
    └── Pasted image.png
```

---

## Troubleshooting

### Connection Issues

**Problem:** Listener doesn't receive connection

**Solutions:**
1. Check firewall settings
2. Verify IP address in `config.py`
3. Ensure both machines on same network
4. Check listener is running before game starts

### Persistence Not Working

**Problem:** Game doesn't start on reboot

**Solutions:**
1. Check file permissions
2. Verify Python path is correct
3. Check system logs for errors
4. Try manual persistence installation

### Game Won't Start

**Problem:** Import errors or crashes

**Solutions:**
1. Ensure all files are present
2. Check Python version (3.7+)
3. Manually install pygame: `pip install pygame`
4. Check file paths in ship.py and alien.py

---

## Presentation Notes

For your March 18, 2026 presentation:

1. **Demo Flow:**
   - Show consent dialog
   - Start listener
   - Run game
   - Execute commands
   - Restart VM to show persistence
   - Run cleanup tool

2. **Key Points to Emphasize:**
   - Ethical considerations
   - Real-world applications
   - Defense mechanisms
   - Transparency through consent

3. **Questions to Prepare For:**
   - How to detect this attack?
   - What makes it stealthy?
   - How would you improve it?
   - What are the legal implications?

---

## Credits

**Team Members:** [Your Names Here]  
**Course:** Cybersecurity  
**Institution:** Rwanda Coding Academy  
**Date:** March 18, 2026  
**Purpose:** Educational Demonstration

---

## License

This software is provided for educational purposes only. Use responsibly and ethically.
