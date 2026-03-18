#!/usr/bin/env python3
"""
Cleanup Tool - Removes all persistence mechanisms
Run this to remove the backdoor from startup programs
"""
import sys
from persistence import PersistenceManager

def main():
    print("=" * 60)
    print("ALIEN INVASION - CLEANUP TOOL")
    print("=" * 60)
    print("\nThis tool will remove all persistence mechanisms installed")
    print("by the Alien Invasion game.\n")
    
    response = input("Do you want to proceed? (yes/no): ").strip().lower()
    
    if response not in ['yes', 'y']:
        print("\nCleanup cancelled.")
        return
    
    print("\nRemoving persistence mechanisms...")
    
    pm = PersistenceManager()
    success = pm.remove_persistence()
    
    if success:
        print("✓ Persistence mechanisms removed successfully!")
        print("\nThe game will no longer start automatically on boot.")
        print("You can safely delete the game folder if desired.")
    else:
        print("✗ Failed to remove some persistence mechanisms.")
        print("You may need to remove them manually.")
        print("\nManual removal instructions:")
        
        if pm.system == 'Linux':
            print("  1. Remove: ~/.config/autostart/alien_invasion.desktop")
            print("  2. Run: crontab -e (and remove any alien_invasion entries)")
        elif pm.system == 'Windows':
            print("  1. Press Win+R, type 'regedit'")
            print("  2. Navigate to: HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
            print("  3. Delete the 'AlienInvasion' entry")
    
    print("\n" + "=" * 60)
    print("Cleanup complete!")
    print("=" * 60)

if __name__ == '__main__':
    main()
