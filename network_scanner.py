import socket
import ipaddress
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor

def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def ping_and_lookup(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]
    result = subprocess.run(command, stdout=subprocess.DEVNULL)
    
    if result.returncode == 0:
        try:
            hostname = socket.gethostbyaddr(str(ip))[0]
        except socket.herror:
            hostname = "unknown host"
        print(f"[+] {ip} is online ({hostname})")
    else:
        print(f"[-] {ip} is offline")

def scan_network():
    local_ip = get_local_ip()
    network = ipaddress.ip_network(local_ip + '/24', strict=False)
    print(f"Scanning network: {network}\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(ping_and_lookup, network.hosts())

if __name__ == "__main__":
    scan_network()
