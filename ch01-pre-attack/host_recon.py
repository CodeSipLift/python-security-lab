import socket
import argparse
import json
import sys

parser = argparse.ArgumentParser(description="Resolve a hostname to an IP address.")
parser.add_argument("hostname", help="Hostname to resolve.")
args = parser.parse_args()

hostname = args.hostname

try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror:
    result = {
        "hostname": hostname,
        "error": "unable to resolve hostname."
    }
    print(json.dumps(result, indent=4))
    sys.exit(1)
else:
    result = {
        "hostname": hostname,
        "ip_address": ip_address
    }
    print(json.dumps(result, indent=4))
    
