# IZEMA 816 - nmap scanner

A Python-based network scanning and monitoring tool built for local network analysis using Nmap and TShark.

---

## What It Does

IZEMA 816 gives you 4 powerful tools in one terminal interface:

| Option | Name | Description |
|--------|------|-------------|
| 1 | SYN ACK Scan | Stealthy TCP scan across ports 1-1024 without completing the handshake |
| 2 | UDP Scan | Discovers hidden services running on UDP ports |
| 3 | Comprehensive Scan | Full version detection + vulnerability scripts via Nmap |
| 4 | Exit|

---

## Requirements

Make sure you have the following installed before running:

- Python 3.x
- Nmap
- TShark (Wireshark CLI)
- python-nmap library

---

## Installation

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/izema816.git
cd izema816
```

**2. Install Python dependencies**
```bash
pip install python-nmap
```

**3. Install Nmap**
```bash
# Debian/Ubuntu
sudo apt install nmap

# Arch
sudo pacman -S nmap

# Mac
brew install nmap
```

**4. Install TShark**
```bash
# Debian/Ubuntu
sudo apt install tshark

# Arch
sudo pacman -S wireshark-cli

# Mac
brew install wireshark
```

---

## How To Run

```bash
sudo python3 izema816.py
```

> Root/sudo is required for SYN scans, UDP scans, and live packet capture.

---

## Usage

When you launch the tool, enter your gateway IP (usually `192.168.1.1`) and pick an option from the menu.

**Example:**
```
Enter Main Gateway IP (e.g., 192.168.1.1): 192.168.1.1

1) SYN ACK Scan
2) UDP Scan
3) Comprehensive Scan
4) Exit

Select an option: 1
```

---

## Legal Disclaimer

> This tool is intended for use on networks you own or have explicit permission to test.
> Unauthorized scanning of networks is illegal in most countries.
> The author holds no responsibility for misuse of this tool.

---

## Author

Made by **IZEMA 816**
