#!/usr/bin/env python3

# Libraries for network packets (scapy) and command-line arguments (argparse).
import scapy.all as scapy
import argparse

def get_arguments():
    """Parses command-line arguments for the target IP range."""
    parser = argparse.ArgumentParser(description="ARP Network Scanner: Scans IP range for active devices.")
    parser.add_argument("-t", "--target", dest='target', help="Target IP address or range (e.g., '192.168.1.0/24').")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Error: Please specify a target IP. Use --help for more info.")
    return options

def scan(ip):
    """
    Performs an ARP scan on the given IP range to discover active devices.

    Args:
        ip (str): Target IP address or CIDR range.

    Returns:
        list: Dictionaries with 'ip' and 'mac' for each discovered client.
    """
    # 1. Craft ARP request packet (pdst: target IP).
    arp_request = scapy.ARP(pdst=ip)
    # 2. Create Ethernet broadcast frame (dst: broadcast MAC).
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # 3. Combine Ethernet frame and ARP request.
    arp_request_broadcast = broadcast / arp_request
    # 4. Send packet and capture responses (Layer 2, timeout 1s, no verbose).
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False) # pylint: disable=unused-variable

    client_list = []
    # 5. Process answered packets: extract IP (psrc) and MAC (hwsrc).
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(results_list):
    """Prints discovered IP and MAC addresses in a formatted table."""
    print("----------------------------------------------------")
    print("IP Address\t\tMAC Address")
    print("----------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])
    print("----------------------------------------------------")

# Execute when script is run directly.
if __name__ == "__main__":
    target_ip_range = get_arguments().target
    scan_result = scan(target_ip_range)
    print_result(scan_result)