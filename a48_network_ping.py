# Network ping

import os

def detect_devices(network):
    print(f"Scanning network: {network}...\n")
    active_devices = []
    for ip in range(1, 255):
        host = f"{network}.{ip}"
        # Command prompt command for Win, 1 ping, w8 1 second, remove default ICMP output messages.
        response = os.system(f"ping -n 1 -w 1000 {host} >nul 2>&1")
        if response == 0:
            active_devices.append(host)
            print(f"Device found: {host}")
    
    if not active_devices:
        print("No active devices found on the network.")
    else:
        print("\nActive devices:")
        for device in active_devices:
            print(device)

detect_devices("192.168.1")

