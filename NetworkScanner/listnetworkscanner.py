#!/usr/bin/env python3

# Import Scapy for network operations.
import scapy.all as scapy

def scan(ip):
    """
    Performs an ARP scan for a given IP range and prints results directly.
    """
    # Create ARP request packet for the target IP range.
    arp_request = scapy.ARP(pdst=ip)
    # Create an Ethernet broadcast frame.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and ARP request.
    arp_request_broadcast = broadcast / arp_request
    # Send the packet and capture responses (Layer 2, timeout 1s, no verbose).
    answered, unanswered = scapy.srp(arp_request_broadcast,timeout=1,verbose=False) # pylint: disable=unused-variable
    
    # Print header for the results.
    print("IP\t\t\tMAC address\n------------------------------------------------")
    # Iterate through answered packets and print IP and MAC.
    for element in answered:
        print(element[1].psrc+"\t\t"+element[1].hwsrc)
        print("-------------------------------------")

# Execute the scan for a placeholder IP range.
# This script is intended for demonstration with a hardcoded IP range.
scan("<ip_address>/24")
