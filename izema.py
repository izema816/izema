import nmap
import socket
import os 

scanner = nmap.PortScanner()

def get_header():
    return "="*60+("\nthis is my nmap scan\n")+"="*60

def clear_screen():
    os.system("clear")
    print(get_header())

ip_addr = input("please enter the main gateaway example: 192.168.1.1: ")

try:
    socket.inet_aton(ip_addr)
except socket.error:
    print("invalid ip")
    exit()

clear_screen()

menu = """
1)tcp
2)udp
3)comprehensive scan
4) exit
"""

while True:
    print(menu)
    response = input("select an option: ").strip()
    
    if response == "1":
        print("[*]Running Tcp scan "+ ip_addr + "....")
        scanner.scan(ip_addr, "1-1024", "-sS")
        if ip_addr in scanner.all_hosts():
            port = list(scanner[ip_addr]["tcp"].keys()) if "tcp" in scanner[ip_addr] else "None"
            print("="*60+ "\nopen ports:\n"+ str(port))
        else:
            print("No results Found")
    
    elif response == "2":
        print("[*]Running Udp scan "+ip_addr + "....")
        scanner.scan(ip_addr, "1-1024", "-sU")
        if ip_addr in scanner.all_hosts():
            port = list(scanner[ip_addr]["udp"].keys()) if "udp" in scanner[ip_addr] else "None"
            print("="*60+"\nopen ports:\n"+ str(port))
        else:
            print("no result found ")
    
    elif response == "3":
        print("[*]Running Comprehensive scan "+ ip_addr + "....")
        scanner.scan(ip_addr, "1-1024", "-sV -sC --script vuln")
        if ip_addr in scanner.all_hosts():
            for proto in scanner[ip_addr].all_protocols():
                print("\nprotocol: "+ proto )
                for port in scanner[ip_addr][proto].keys():
                    state = scanner[ip_addr][proto][port]["state"]
                    name = scanner[ip_addr][proto][port]["name"]
                    ver = scanner[ip_addr][proto][port].get("version", "")
                    print("port: " + str(port) + "|" + state + "|" + name + "|" + ver )
    
    elif response == "4":
        print("shutting down.......")
        break
    
    else:
       print("invalid option choose 1 to 4 !")
