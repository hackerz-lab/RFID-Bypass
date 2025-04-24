#!/usr/bin/env python3
# RFID Signal Simulator - For Educational and Testing Purposes Only

import os
import time
import random
import argparse
from sys import platform
from datetime import datetime

# ANSI Color Codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ASCII Art Banner
BANNER = f"""
{Colors.RED}╦═╗╔═╗╔╦╗╔═╗  ╔═╗┌─┐┌┬┐┌─┐┬─┐┌─┐┌─┐┬ ┬
{Colors.RED}╠╦╝║╣  ║ ║ ║  ╚═╗├┤  │ ├─┤├┬┘├┤ └─┐├─┤
{Colors.RED}╩╚═╚═╝ ╩ ╚═╝  ╚═╝└─┘ ┴ ┴ ┴┴└─└─┘└─┘┴ ┴
{Colors.CYAN}╔════════════════════════════════════════════╗
{Colors.CYAN}║     RFID FREQUENCY PRO v1.3.7       ║
{Colors.CYAN}║       {Colors.RED}FOR EDUCATIONAL PURPOSES ONLY{Colors.CYAN}        ║
{Colors.CYAN}╚════════════════════════════════════════════╝
{Colors.RESET}"""

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    clear_screen()
    print(BANNER)
    print(f"{Colors.YELLOW}[*] Initialization RFID Signal Reading Engine...{Colors.RESET}\n")

def generate_rfid_code(rfid_type="EM4100"):
    """Generate realistic-looking RFID codes based on common formats"""
    formats = {
        "EM4100": lambda: ''.join(random.choices("0123456789ABCDEF", k=10)),
        "HID": lambda: f"{random.randint(2000, 9999)}"+''.join(random.choices("0123456789", k=6)),
        "MIFARE": lambda: ''.join(random.choices("0123456789ABCDEF", k=8)),
        "ISO14443": lambda: ''.join(random.choices("0123456789ABCDEF", k=16))
    }
    return formats.get(rfid_type, formats["EM4100"])()

def simulate_signal_transmission(code, rfid_type, power=100, frequency=125):
    """Writing the process of transmitting an RFID signal"""
    steps = [
        (f"Configuring {rfid_type} protocol", 1.5),
        (f"Setting frequency to {frequency} kHz", 1),
        (f"Adjusting power to {power}%", 0.5),
        ("Generating carrier wave", 1.2),
        ("Modulating data signal", 1.8),
        ("Transmitting RFID code", 2),
        ("Verifying signal integrity", 1.5)
    ]

    print(f"\n{Colors.BLUE}[+] Preparing to transmit RFID code: {Colors.BOLD}{code}{Colors.RESET}")
    print(f"{Colors.PURPLE} |_ Type: {rfid_type}\n |_ Power: {power}%\n |_ Frequency: {frequency} kHz{Colors.RESET}\n")

    for step, duration in steps:
        print(f"{Colors.CYAN}[~] {step}...", end='', flush=True)
        time.sleep(duration * random.uniform(0.8, 1.2))
        print(f"{Colors.GREEN} ✓{Colors.RESET}")

    print(f"\n{Colors.GREEN}[✓] RFID signal transmitted successfully at {datetime.now().strftime('%H:%M:%S')}{Colors.RESET}")

def main():
    parser = argparse.ArgumentParser(description='RFID Signal Simulator Pro')
    parser.add_argument('-t', '--type', choices=['EM4100', 'HID', 'MIFARE', 'ISO14443'], 
                       default='EM4100', help='RFID tag type to simulate')
    parser.add_argument('-p', '--power', type=int, choices=range(1, 101), 
                       default=80, help='Transmission power percentage (1-100)')
    parser.add_argument('-f', '--frequency', type=int, 
                       default=125, help='Frequency in kHz (default: 125)')
    parser.add_argument('-c', '--code', help='Specific RFID code to use')
    parser.add_argument('-a', '--auto', action='store_true', 
                       help='Auto-transmit without confirmation')
    args = parser.parse_args()

    print_banner()

    # Generate or use provided code
    rfid_code = args.code if args.code else generate_rfid_code(args.type)

    print(f"{Colors.YELLOW}[*] RFID Signal Parameters:{Colors.RESET}")
    print(f" |_ Type: {Colors.BLUE}{args.type}{Colors.RESET}")
    print(f" |_ Code: {Colors.BLUE}{rfid_code}{Colors.RESET}")
    print(f" |_ Power: {Colors.BLUE}{args.power}%{Colors.RESET}")
    print(f" |_ Frequency: {Colors.BLUE}{args.frequency} kHz{Colors.RESET}")

    if not args.auto:
        confirm = input(f"\n{Colors.YELLOW}[?] Begin transmission? (y/n): {Colors.RESET}").lower()
        if confirm != 'y':
            print(f"{Colors.RED}[-] Transmission aborted{Colors.RESET}")
            return

    simulate_signal_transmission(rfid_code, args.type, args.power, args.frequency)

    print(f"\n{Colors.YELLOW}[!] Disclaimer:{Colors.RESET}")
  #  print(f"{Colors.WHITE}This is a simulation only. No actual RFID signals are transmitted.")
   # print(f"Real RFID systems implement security measures that prevent unauthorized access.{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[-] Transmission interrupted by user{Colors.RESET}")
        exit(0)
