import socket
import threading

target = input("Enter target IP: ")

try:
    target = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved")
    exit()

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
print(f"\nStarting scan on {target}\n")
threads = []

def scan_port(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0 :
        print(f"Port {port} is OPEN")
    
    s.close()
    
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()
        
for thread in threads:
    thread.join()
    
print("\nScan completed.")