#!/usr/bin/env python3
# RFID Security Bypass - For Educational Purposes Only

import os
import time
import random
from sys import platform
import argparse

# ASCII Art and Colors
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

BANNER = f"""
{Colors.RED}╔╦╗╦═╗╔═╗╔═╗  ╔╗ ┌─┐┌─┐┌─┐┬ ┬┬─┐┌─┐┬─┐
{Colors.RED} ║ ╠╦╝╠═╣║╣   ╠╩╗├─┤│  ├─┘│ │├┬┘├┤ ├┬┘
{Colors.RED} ╩ ╩╚═╩ ╩╚═╝  ╚═╝┴ ┴└─┘┴  └─┘┴└─└─┘┴└─
{Colors.CYAN}╔════════════════════════════════════════╗
{Colors.CYAN}║    RFID SECURITY BYPASS      ║
{Colors.CYAN}║       {Colors.RED}FOR EDUCATIONAL PURPOSES ONLY{Colors.CYAN}      ║
{Colors.CYAN}╚════════════════════════════════════════╝
{Colors.RESET}"""

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    clear_screen()
    print(BANNER)
    print(f"{Colors.YELLOW}[*] Initializing RFID Bypass Sequence...{Colors.RESET}\n")

def simulate_hacking():
    steps = [
        ("Scanning for RFID signals", 2),
        ("Intercepting transmission", 3),
        ("Analyzing frequency patterns", 2),
        ("Brute-forcing RFID codes", 4),
        ("Cracking encryption", 3),
        ("Generating clone signal", 2),
        ("Bypassing security protocols", 3),
        ("Injecting malicious payload", 2)
    ]

    for step, duration in steps:
        print(f"{Colors.BLUE}[+] {step}...", end='', flush=True)
        time.sleep(duration)
        print(f"{Colors.GREEN} DONE!{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}[!] RFID SECURITY BYPASSED SUCCESSFULLY!{Colors.RESET}")

def generate_rfid_code():
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(10))

def main():
    parser = argparse.ArgumentParser(description='RFID Security Bypass Simulator')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-s', '--simulate', action='store_true', help='Simulate full bypass process')
    args = parser.parse_args()

    print_banner()

    if args.simulate or input(f"{Colors.YELLOW}[?] Start simulation? (y/n): {Colors.RESET}").lower() == 'y':
        simulate_hacking()
        
        rfid_code = generate_rfid_code()
        print(f"\n{Colors.PURPLE}[*] Generated Clone RFID Code: {Colors.BOLD}{rfid_code}{Colors.RESET}")
        
        # print(f"\n{Colors.YELLOW}[!] WARNING: This is a Highly Dangerous.{Colors.RESET}")
        # print(f"{Colors.YELLOW}[!] Actual RFID systems have stronger security measures.{Colors.RESET}")
    else:
        print(f"{Colors.RED}[-] Operation Finished.{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[-] Process interrupted by user.{Colors.RESET}")
        exit(0)
