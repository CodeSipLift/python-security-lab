import socket
import argparse

parser = argparse.ArgumentParser(description="Resolve a hostname to an IP address.")
parser.add_argument("hostname", help="Hostname to resolve.")
args = parser.parse_args()

hostname = args.hostname

try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror:
    print("Error: Unable to resolve hostname.")
else:
    print(f"Target: {hostname}")
    print(f"IP Address: {ip_address}")
    
