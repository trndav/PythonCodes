'''
Scans IPs on network.
Works on Win systems.
Does not detect wifi device ips.
'''

import os
import platform
import socket
from concurrent.futures import ThreadPoolExecutor

param = "-n" if platform.system().lower() == "windows" else "-c"

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def ping(ip):
    if platform.system().lower() == "windows":
        response = os.system(f"ping {param} 1 -w 500 {ip} > nul")
    else:
        response = os.system(f"ping {param} 1 -W 1 {ip} > /dev/null 2>&1")
    return ip if response == 0 else None

def scan_subnet(base_ip):
    print(f"Scanning {base_ip}.0/24...")
    ips = [f"{base_ip}.{i}" for i in range(1, 255)]
    active = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(ping, ips)
        active = [ip for ip in results if ip]

    return active

def main():
    local_ip = get_local_ip()
    base_ip = ".".join(local_ip.split(".")[:3])
    active_hosts = scan_subnet(base_ip)

    print("\nActive IPs on network:")
    for ip in active_hosts:
        print(ip)

if __name__ == "__main__":
    main()
