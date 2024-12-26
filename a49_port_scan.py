# Port scan

import socket

def scan_port(target_host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except:
        pass

target_host = "192.168.1.1"
port_range = range(1, 100)

for port in port_range:
    scan_port(target_host, port)