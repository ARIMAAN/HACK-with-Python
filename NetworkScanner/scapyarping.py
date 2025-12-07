#!/usr/bin/enc python3

# Import Scapy for network operations.
import scapy.all as scapy

def scan(ip):
    """
    Performs a simple ARP scan using Scapy's arping function.
    This function sends ARP requests and prints responses directly.
    """
    scapy.arping(ip)

# Execute the scan with a placeholder IP.
# This script is intended for demonstration with a specific IP.
scan("<ip_address>")