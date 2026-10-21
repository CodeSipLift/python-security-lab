import socket

hostname = input("Enter a hostname: ")

try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror:
    print("Error: Unable to resolve hostname.")
else:
    print(f"Target: {hostname}")
    print(f"IP Address: {ip_address}")
    
