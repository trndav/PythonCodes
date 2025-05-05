import socket

def scan_ports(ip, ports):
    print(f"Scanning {ip} on ports: {ports}")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            s.close()
        except KeyboardInterrupt:
            print("\nScan stopped by user.")
            break
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# Example usage
target_ip = input("Enter IP to scan: ")
common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3306, 3389]
scan_ports(target_ip, common_ports)
