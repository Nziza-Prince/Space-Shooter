#!/usr/bin/env python3
"""
Simple connection test - Run this on Windows to test if backdoor can connect
"""
import socket
import sys

LISTENER_HOST = '10.12.72.171'  # Your Kali IP
LISTENER_PORT = 4444

print("="*60)
print("Connection Test")
print("="*60)
print(f"\nTrying to connect to {LISTENER_HOST}:{LISTENER_PORT}...")
print()

try:
    # Try to connect
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect((LISTENER_HOST, LISTENER_PORT))
    
    print("✓ CONNECTION SUCCESSFUL!")
    print(f"✓ Connected to {LISTENER_HOST}:{LISTENER_PORT}")
    print()
    print("The backdoor should work!")
    
    # Send test message
    sock.send(b"whoami\n")
    response = sock.recv(1024)
    print(f"\nReceived: {response.decode()}")
    
    sock.close()
    
except socket.timeout:
    print("✗ CONNECTION TIMEOUT")
    print("The listener is not responding.")
    print()
    print("Possible issues:")
    print("  - Firewall blocking connection")
    print("  - Wrong IP address")
    print("  - Listener not running")
    
except ConnectionRefusedError:
    print("✗ CONNECTION REFUSED")
    print("The listener is not running on that port.")
    print()
    print("Make sure listener.py is running on Kali")
    
except Exception as e:
    print(f"✗ CONNECTION FAILED: {e}")
    print()
    print("Possible issues:")
    print("  - Not on same network")
    print("  - Firewall blocking")
    print("  - Wrong IP/port")

print()
print("="*60)
input("Press Enter to exit...")
