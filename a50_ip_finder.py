# Check ip

import socket

def get_local_ip():
    # Get the local machine's IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Your local IP address is: {local_ip}")

def get_host_ip():
    # Get the IP address of a specified host
    host = input("Enter a hostname (e.g., google.com): ")
    try:
        host_ip = socket.gethostbyname(host)
        print(f"The IP address of {host} is: {host_ip}")
    except socket.gaierror:
        print(f"Unable to get the IP address for {host}.")

# Run the functions
get_local_ip()
get_host_ip()
