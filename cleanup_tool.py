#!/usr/bin/env python3
"""
Cleanup Tool - Removes all persistence mechanisms and backdoor processes
Run this to completely remove the backdoor from the system
"""
import sys
import os
import subprocess
import platform
from persistence import PersistenceManager

def kill_backdoor_processes():
    """Kill any running backdoor processes"""
    system = platform.system()
    killed = False
    
    try:
        if system == 'Windows':
            # Kill python processes running backdoor
            print("  Checking for python processes...")
            
            # Kill pythonw processes (backdoor runs with pythonw)
            try:
                result = subprocess.run(
                    ['taskkill', '/F', '/IM', 'pythonw.exe'],
                    capture_output=True,
                    text=True
                )
                if 'SUCCESS' in result.stdout:
                    print("  ✓ Killed pythonw.exe processes")
                    killed = True
            except:
                pass
            
            # Kill python processes
            try:
                result = subprocess.run(
                    ['taskkill', '/F', '/IM', 'python.exe'],
                    capture_output=True,
                    text=True
                )
                if 'SUCCESS' in result.stdout:
                    print("  ✓ Killed python.exe processes")
                    killed = True
            except:
                pass
            
            # Kill AlienInvasion processes
            try:
                subprocess.run(['taskkill', '/F', '/IM', 'AlienInvasion.exe'], 
                             capture_output=True)
                subprocess.run(['taskkill', '/F', '/IM', 'AlienInvasion-Console.exe'], 
                             capture_output=True)
                killed = True
            except:
                pass
            
        else:  # Linux
            # Kill processes with alien_invasion in name
            try:
                subprocess.run(['pkill', '-f', 'alien_invasion'], capture_output=True)
                subprocess.run(['pkill', '-f', 'backdoor'], capture_output=True)
                subprocess.run(['pkill', '-f', 'game_update'], capture_output=True)
                killed = True
            except:
                pass
    except Exception as e:
        print(f"  Warning: Could not kill all processes: {e}")
    
    return killed

def remove_temp_files():
    """Remove temporary backdoor files"""
    import tempfile
    import glob
    
    temp_dir = tempfile.gettempdir()
    removed = 0
    
    # Look for backdoor temp files
    patterns = [
        os.path.join(temp_dir, 'tmp*.py'),
        os.path.join(temp_dir, '*backdoor*.py'),
    ]
    
    for pattern in patterns:
        for file in glob.glob(pattern):
            try:
                # Check if file contains backdoor code
                with open(file, 'r') as f:
                    content = f.read()
                    if 'LISTENER_HOST' in content or 'backdoor' in content.lower():
                        os.remove(file)
                        removed += 1
            except:
                pass
    
    return removed

def remove_persistence_entries():
    """Remove Windows registry persistence entries"""
    removed = []
    try:
        import winreg
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        
        print("  Checking registry entries...")
        
        # Remove both old and new entries
        for entry_name in ["AlienInvasion", "SystemUpdate"]:
            try:
                winreg.DeleteValue(key, entry_name)
                removed.append(entry_name)
                print(f"  ✓ Removed registry entry: {entry_name}")
            except FileNotFoundError:
                print(f"  ℹ Entry not found: {entry_name}")
        
        winreg.CloseKey(key)
        
        # Also remove the persistent backdoor file
        import os
        persistent_backdoor = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'SystemUpdate', 'update.pyw')
        print(f"  Checking for: {persistent_backdoor}")
        
        if os.path.exists(persistent_backdoor):
            os.remove(persistent_backdoor)
            removed.append("Persistent backdoor file")
            print(f"  ✓ Removed: {persistent_backdoor}")
        else:
            print(f"  ℹ File not found: {persistent_backdoor}")
        
        # Remove the directory if empty
        backdoor_dir = os.path.dirname(persistent_backdoor)
        if os.path.exists(backdoor_dir):
            try:
                if not os.listdir(backdoor_dir):
                    os.rmdir(backdoor_dir)
                    print(f"  ✓ Removed directory: {backdoor_dir}")
            except:
                pass
        
        # Also check temp directory for backdoor scripts
        import tempfile
        temp_backdoor = os.path.join(tempfile.gettempdir(), 'game_update.pyw')
        if os.path.exists(temp_backdoor):
            os.remove(temp_backdoor)
            removed.append("Temp backdoor file")
            print(f"  ✓ Removed: {temp_backdoor}")
            
    except Exception as e:
        print(f"  Error removing persistence: {e}")
    
    return removed

def main():
    print("=" * 60)
    print("ALIEN INVASION - CLEANUP TOOL")
    print("=" * 60)
    print("\nThis tool will remove all traces of the backdoor:")
    print("  • Kill running backdoor processes")
    print("  • Remove persistence mechanisms (autostart)")
    print("  • Remove temporary files")
    print("  • Clean up registry entries (Windows)")
    print()
    
    response = input("Do you want to proceed? (yes/no): ").strip().lower()
    
    if response not in ['yes', 'y']:
        print("\nCleanup cancelled.")
        return
    
    print("\n" + "=" * 60)
    print("CLEANING UP...")
    print("=" * 60)
    
    # Step 1: Kill backdoor processes
    print("\n[1/4] Killing backdoor processes...")
    if kill_backdoor_processes():
        print("  ✓ Backdoor processes terminated")
    else:
        print("  ℹ No backdoor processes found")
    
    # Step 2: Remove persistence
    print("\n[2/4] Removing persistence mechanisms...")
    pm = PersistenceManager()
    pm.remove_persistence()
    
    # Also remove new persistence entries
    removed_entries = remove_persistence_entries()
    if removed_entries:
        print(f"  ✓ Removed: {', '.join(removed_entries)}")
    else:
        print("  ℹ No persistence entries found")
    
    # Step 3: Remove temp files
    print("\n[3/4] Removing temporary files...")
    removed = remove_temp_files()
    if removed > 0:
        print(f"  ✓ Removed {removed} temporary file(s)")
    else:
        print("  ℹ No temporary files found")
    
    # Step 4: Verify cleanup
    print("\n[4/4] Verifying cleanup...")
    
    system = platform.system()
    issues = []
    
    if system == 'Linux':
        # Check autostart
        autostart_file = os.path.expanduser('~/.config/autostart/alien_invasion.desktop')
        if os.path.exists(autostart_file):
            issues.append("Autostart file still exists")
        
        # Check crontab
        try:
            result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
            if 'alien_invasion' in result.stdout:
                issues.append("Cron job still exists")
        except:
            pass
    
    elif system == 'Windows':
        # Check registry
        try:
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                winreg.KEY_READ
            )
            # Check for both old and new persistence entries
            for entry_name in ["AlienInvasion", "SystemUpdate"]:
                try:
                    winreg.QueryValueEx(key, entry_name)
                    issues.append(f"Registry entry '{entry_name}' still exists")
                except FileNotFoundError:
                    pass
            winreg.CloseKey(key)
        except:
            pass
    
    if issues:
        print("  ⚠ Issues found:")
        for issue in issues:
            print(f"    - {issue}")
    else:
        print("  ✓ System is clean")
    
    print("\n" + "=" * 60)
    print("CLEANUP COMPLETE!")
    print("=" * 60)
    
    if issues:
        print("\nManual cleanup required:")
        print()
        
        if system == 'Linux':
            print("Run these commands:")
            print("  rm ~/.config/autostart/alien_invasion.desktop")
            print("  crontab -e  # Remove alien_invasion lines")
        
        elif system == 'Windows':
            print("Manual steps:")
            print("  1. Press Win+R, type 'regedit'")
            print("  2. Navigate to: HKEY_CURRENT_USER\\Software\\Microsoft\\")
            print("     Windows\\CurrentVersion\\Run")
            print("  3. Delete 'AlienInvasion' entry")
    else:
        print("\n✓ All backdoor components have been removed!")
        print("✓ Your system is clean")
        print("\nThe game folder can now be safely deleted.")
    
    print("\n" + "=" * 60)
    input("\nPress Enter to exit...")

if __name__ == '__main__':
    main()
