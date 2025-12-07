#!/usr/bin/env python3

# Import Scapy for network operations.
import scapy.all as scapy

def scan(ip):
    """
    Performs an ARP scan for a given IP range and returns a list of discovered clients.
    """
    # Create ARP request packet for the target IP range.
    arp_request = scapy.ARP(pdst=ip)
    # Create an Ethernet broadcast frame.
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and ARP request.
    arp_request_broadcast=broadcast/arp_request
    # Send the packet and capture responses (Layer 2, timeout 1s, no verbose).
    answered, unanswered = scapy.srp(arp_request_broadcast,timeout=1,verbose=False) # pylint: disable=unused-variable
    
    client_list=[]    
    # Process answered packets: extract IP (psrc) and MAC (hwsrc).
    for element in answered:
        client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(results_list):
    """Prints discovered IP and MAC addresses in a formatted table."""
    # Print header for the results.
    print("IP\t\t\tMAC address\n------------------------------------------------")
    # Iterate through the list of clients and print their details.
    for client in results_list:
        print(client["ip"]+"\t\t"+client["mac"])

# Execute the scan for a placeholder IP range and print results.
# This script is intended for demonstration with a hardcoded IP range.
scan_result=scan("<ip_address>/24")
print_result(scan_result)