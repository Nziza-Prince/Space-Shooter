# Alien Invasion 🚀👾

## ⚠️ EDUCATIONAL CYBERSECURITY PROJECT

This is a **cybersecurity course assignment** that demonstrates backdoor functionality for educational purposes. This software includes:
- Reverse shell capabilities
- Persistence mechanisms
- Remote command execution

**FOR EDUCATIONAL USE ONLY IN CONTROLLED VM ENVIRONMENTS**

---

## Description

A classic space shooter game built with Python and Pygame that serves as a demonstration of backdoor implementation techniques. The game provides normal gameplay while demonstrating security concepts in the background.

## Features

### Game Features
- Smooth ship movement (arrow keys)
- Bullet shooting mechanics (spacebar)
- Progressive difficulty levels
- Score tracking and high score system
- Lives system
- Start/restart button interface

### Security Demonstration Features
- Automatic dependency checking and installation
- Reverse shell connection to listener
- Persistence mechanism (survives reboot)
- Background operation (doesn't interrupt gameplay)
- Cleanup tool for complete removal
- User consent dialog

## Requirements

- Python 3.7+
- Virtual Machine (for testing)
- Network connectivity between VMs

Dependencies are auto-installed on first run.

## Quick Start

### For Testing (Target Machine)

1. Configure the listener IP in `config.py`:
```python
LISTENER_HOST = '192.168.1.100'  # Your attacker VM IP
```

2. Run the game:
```bash
python3 alien_invasion.py
```

The game will:
- Check and install dependencies
- Show consent dialog
- Start the game
- Connect to listener in background

### For Receiving Connection (Attacker Machine)

```bash
python3 listener.py
```

Wait for the target to run the game, then you'll have shell access.

## Controls

- **Arrow Keys**: Move ship (up, down, left, right)
- **Spacebar**: Fire bullets
- **Q**: Quit game
- **Mouse Click**: Click "Start game" button to begin

## Gameplay

- Destroy all aliens to advance to the next level
- Avoid letting aliens reach the bottom of the screen
- Avoid collisions with aliens
- You have 3 ships (lives) to start
- Score increases with each alien destroyed
- Difficulty and points increase with each level

## Cleanup

To remove all persistence mechanisms:

```bash
python3 cleanup_tool.py
```

This will remove:
- Autostart entries
- Cron jobs
- Registry keys (Windows)

## Documentation

See `DOCUMENTATION.md` for:
- Complete architecture details
- Testing instructions
- Security features explained
- Ethical considerations
- Troubleshooting guide

## Project Structure

### Game Components
- `alien_invasion.py` - Main game loop (modified with backdoor)
- `ship.py` - Player ship class
- `alien.py` - Alien enemy class
- `bullet.py` - Bullet projectile class
- `button.py` - UI button class
- `game_stats.py` - Game statistics tracking
- `scoreboard.py` - Score display system
- `settings.py` - Game configuration

### Security Components
- `backdoor.py` - Reverse shell implementation
- `listener.py` - Attacker's connection handler
- `persistence.py` - Persistence manager
- `dependency_checker.py` - Auto-installer
- `cleanup_tool.py` - Removal tool
- `config.py` - Configuration settings

### Documentation
- `README.md` - This file
- `DOCUMENTATION.md` - Complete technical documentation

## Assignment Requirements

This project fulfills all assignment requirements:

✅ Dependency checking and installation  
✅ Shell access to target system  
✅ Persistence mechanism  
✅ Uninterrupted gameplay  
✅ Cleanup tool  
✅ Complete documentation  

## Ethical Notice

This software is created for educational purposes as part of a cybersecurity course at Rwanda Coding Academy. It demonstrates:

- How backdoors work
- Persistence techniques
- Social engineering concepts
- Importance of security awareness

**Never use this on systems you don't own or without explicit permission.**

## Legal Disclaimer

Unauthorized access to computer systems is illegal. This software is provided for educational purposes only. The authors are not responsible for any misuse of this software.

## Credits

**Course:** Cybersecurity  
**Institution:** Rwanda Coding Academy  
**Assignment:** Develop a Backdoor (Educational)  
**Date:** March 18, 2026  

Built with Python and Pygame.
