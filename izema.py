import nmap
import os

scanner = nmap.PortScanner()

def get_header():
    return "="*60 + "\n IZEMA 816 - THE ULTIMATE NETWORK & DEFENDER \n" + "="*60

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

clear_screen()
print(get_header())

ip_addr = input("\nEnter Main Gateway IP (e.g., 192.168.1.1): ")

menu = """
1) SYN ACK Scan (Fast/Stealth)
2) UDP Scan (Find hidden services)
3) Comprehensive Scan (Versions & Vulnerabilities)
4) Exit
"""

while True:
    print("\n" + "-"*30)
    print(menu)
    resp = input("Select an option: ").strip()

    if resp == "1":
        print("\n[*] Running SYN ACK Scan on " + ip_addr + "...")
        scanner.scan(ip_addr, "1-1024", "-v -sS")
        if ip_addr in scanner.all_hosts():
            ports = list(scanner[ip_addr]["tcp"].keys()) if "tcp" in scanner[ip_addr] else "None"
            print("Open Ports: " + str(ports))

    elif resp == "2":
        print("\n[*] Running UDP Scan on " + ip_addr + "...")
        scanner.scan(ip_addr, "1-1024", "-sU")
        if ip_addr in scanner.all_hosts():
            ports = list(scanner[ip_addr]["udp"].keys()) if "udp" in scanner[ip_addr] else "None"
            print("Open UDP Ports: " + str(ports))

    elif resp == "3":
        print("\n[*] Running Comprehensive Scan on " + ip_addr + "...")
        scanner.scan(ip_addr, "1-1024", "-sV -sC --script vuln")
        if ip_addr in scanner.all_hosts():
            for proto in scanner[ip_addr].all_protocols():
                print("\nProtocol: " + proto)
                for port in scanner[ip_addr][proto].keys():
                    state = scanner[ip_addr][proto][port]["state"]
                    name  = scanner[ip_addr][proto][port]["name"]
                    ver   = scanner[ip_addr][proto][port].get("version", "")
                    print("  Port " + str(port) + ": " + state + " | " + name + " " + ver)

    elif resp == "4":
        print("Powering down.")
        break
    else:
        print("Invalid option. Please choose 1-4.")
