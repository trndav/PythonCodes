# Ping multiple hosts

import os

def ping_hosts():
    hosts = ["google.com", "facebook.com", "bing.com", "dkrj593jedlvt.com"]
    for host in hosts:
        response = os.system(f"ping -n 1 -w 1000 {host} >nul 2>&1")
        if response == 0:
            print(f"{host} is available.")
        else:
            print(f"{host} is not available.")

ping_hosts()