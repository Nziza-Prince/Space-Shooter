#!/bin/bash
# Build Windows .exe from Linux using Wine

echo "=========================================="
echo "Building Windows .exe using Wine"
echo "=========================================="
echo ""

# Check if Wine is installed
if ! command -v wine &> /dev/null; then
    echo "Wine is not installed. Installing..."
    echo ""
    sudo dpkg --add-architecture i386
    sudo apt update
    sudo apt install -y wine wine64 wine32
fi

echo "Wine version:"
wine --version
echo ""

# Download Python for Windows if not exists
PYTHON_INSTALLER="python-3.11.0-amd64.exe"
if [ ! -f "$PYTHON_INSTALLER" ]; then
    echo "Downloading Python for Windows..."
    wget https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
fi

echo ""
echo "Note: This process is complex and may not work perfectly."
echo "Recommended: Build on an actual Windows machine instead."
echo ""
echo "Alternative: Use GitHub Actions or a Windows VM"
