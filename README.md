# 📡 SPECTER: Ghost Network Recon Engine

> **⚠️ ARCH LINUX EXCLUSIVE**
> *This tool is strictly built and optimized for Arch Linux and its derivatives (EndeavourOS, Manjaro, BlackArch). It leverages native raw socket injection and PEP 517 build standards. Execution on non-Arch systems is explicitly locked and not supported.*

**SPECTER** is an advanced, standalone network reconnaissance engine designed to detect exposed infrastructure and IoT devices (such as RTSP streams and IP cameras). By dropping reliance on third-party APIs (like Shodan), SPECTER operates entirely locally, utilizing **Ghost Mode (Stealth SYN Scanning)** to bypass firewalls and minimize footprint on Intrusion Detection Systems (IDS).

## ⚙️ Tech Stack
- **Language:** Python 3.12+
- **Build System:** PEP 517 (python-build, python-installer, wheel)
- **Primary Engine:** Nmap (Stealth SYN Scanning via subprocess)
- **UI Framework:** Rich (Tactical Terminal UI)

## 🚀 Key Features
- **Independent Radar:** No API Keys required. Scans directly from your local machine using raw network sockets.
- **Ghost Mode (Stealth):** Utilizes Nmap's SYN Scan (`-sS`) and Polite Timing template (`-T2`) to evade ISP monitoring and firewalls.
- **Tactical UI:** Color-coded, rapid-parsing terminal output using the Rich library, optimized for active operations.
- **Arch Native:** Fully integrated with `makepkg` and AUR distribution standards.

---

## 🛠️ Installation (The Arch Way)

Ensure your system has the base development tools (`base-devel`) and an AUR helper installed. SPECTER requires `nmap` and `python` to function.

### 1. Clone the repository
```bash
git clone [https://github.com/LoudLunatics/specter.git](https://github.com/LoudLunatics/specter.git)
cd specter

2. Build and Install via makepkg

Run the following command to automatically resolve dependencies, build the Python package, and install it to your Arch system:
Bash

makepkg -si

    💡 Troubleshooting (Validity Check Failed):
    If you encounter a "One or more files did not pass the validity check!" error during installation, it means the checksums in the PKGBUILD are outdated. Run these commands to fix it:
    Bash

    rm -rf src/ pkg/ specter-*.tar.gz
    updpkgsums
    makepkg --printsrcinfo > .SRCINFO
    makepkg -si

💻 Usage

Because SPECTER relies on Stealth SYN Scanning—which manipulates raw TCP packets—the engine must be executed with root (sudo) privileges.
Bash

sudo specter

Modes of Operation

Upon execution, SPECTER will prompt you for two parameters:

    Target IP / Range: You can input a single IP (e.g., 192.168.1.1) or a CIDR subnet (e.g., 103.10.0.0/24).

    Stealth Mode (y/n):

        y (GHOST): Uses slower timing (-T2) to remain undetected. Recommended for public networks.

        n (NORMAL): Uses standard timing (-T3) for much faster execution. Recommended for local/home networks.

Example Output
Plaintext

  _____ _____  ______ _____ _______ ______ _____  
 / ____|  __ \|  ____/ ____|__   __|  ____|  __ \ 
| (___ | |__) | |__ | |       | |  | |__  | |__) |
 \___ \|  ___/|  __|| |       | |  |  __| |  _  / 
 ____) | |    | |___| |____   | |  | |____| | \ \ 
|_____/|_|    |______\_____|  |_|  |______|_|  \_\

        >> NETWORK RECONNAISSANCE & INFILTRATION ENGINE <<
Version 1.2.2 | Authorized Red Team Access Only
——————————————————————————————————————————————————————————————————————

SPECTER@target_ip/range: 192.168.1.0/24
SPECTER@stealth_mode(y/n): y

[*] Scanning target 192.168.1.0/24 in GHOST mode...
⠧ Infiltrating network...

TARGETS ACQUIRED (3 found)
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┓
┃ IP Address      ┃ Organization              ┃ Port ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━┩
│ 192.168.1.1     │ Gateway/Router            │  554 │
│ 192.168.1.15    │ Infiltrated Host          │  554 │
│ 192.168.1.22    │ Infiltrated Host          │  554 │
└─────────────────┴───────────────────────────┴──────┘

[+] Reconnaissance complete.

🛡️ Disclaimer

This project is developed strictly for educational purposes and ethical security research. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Always adhere to local cybersecurity laws and obtain proper authorization before scanning networks you do not own.
