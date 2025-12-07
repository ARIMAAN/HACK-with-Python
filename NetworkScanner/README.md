# NetworkScanner - About and How to Run

## What it Does

This `NetworkScanner` project provides a Python-based tool to perform an ARP (Address Resolution Protocol) scan on a local network. It identifies active devices within a specified IP address or IP range by sending ARP requests and parsing their responses. This tool is fundamental for network reconnaissance, allowing you to discover the IP and MAC addresses of devices connected to your network.

**Note on Scripts**: The primary script for a generic, command-line driven scan is `run_networkscanner.py`. Other scripts like `scapyarping.py`, `listnetworkscanner.py`, and `networkscanner.py` demonstrate simpler, often hardcoded, variations of network scanning for educational purposes.

## Features

*   **ARP-based Scanning**: Uses ARP requests to discover devices on a local network.
*   **IP Range Support**: Scans single IP addresses or entire IP subnets (e.g., `CIDR notation`).
*   **IP and MAC Address Discovery**: Reports IP and corresponding MAC addresses for responsive devices.
*   **Command-line Interface**: Easy to use via command line, accepts target IP range as argument (in `run_networkscanner.py`).
*   **Minimal Dependencies**: Primarily relies on the `scapy` library.

## How it Works (Technical Details)

The `run_networkscanner.py` script (the main generic scanner) operates by performing the following steps:

1.  **Argument Parsing**: Parses command-line arguments to get the target IP address or range.
2.  **ARP Request Construction**:
    *   Constructs an `ARP` request packet with `pdst` (protocol destination) set to the target IP(s).
    *   Creates an `Ethernet` frame with `dst` (destination MAC) set to `ff:ff:ff:ff:ff:ff` (broadcast).
    *   Combines these: `broadcast / arp_request`.
3.  **Packet Sending and Receiving**:
    *   Sends the combined packet using Scapy's Layer 2 `srp()` function.
    *   Sets `timeout=1` and `verbose=False`.
4.  **Response Processing**:
    *   `srp()` returns `answered_list` (received responses).
    *   Iterates through `answered_list`, extracting `psrc` (source IP) and `hwsrc` (source MAC) from each response.
    *   Stores IP-MAC pairs in a list of dictionaries.
5.  **Result Display**: Prints the collected IP-MAC pairs in a clear, tabular format.

## How to Run

Follow these steps to set up and run the NetworkScanner script (`run_networkscanner.py`):

1.  **Navigate to the project directory:**
    Open your terminal or command prompt and change your current directory to the `NetworkScanner` folder:
    ```bash
    cd "f:\Python Hacking\HACK with Python\NetworkScanner"
    ```

2.  **Install Dependencies:**
    This script requires the `scapy` library. If you do not have it installed, you can do so using pip:
    ```bash
    pip install scapy
    ```
    (If you have multiple Python versions, you might need to use `pip3 install scapy`.)

3.  **Execute the primary script (`run_networkscanner.py`):**
    Run the Python script from your terminal, providing the target IP address or range using the `-t` or `--target` argument.

    ```bash
    python run_networkscanner.py -t <target_ip_address_or_range>
    ```

    **Examples:**

    *   **Scan a specific IP address:**
        ```bash
        python run_networkscanner.py -t <ip_address>
        ```

    *   **Scan an entire subnet:**
        ```bash
        python run_networkscanner.py -t <ip_address>/24
        ```

    **To run other simpler scripts:**
    *   `scapyarping.py`: Directly uses `scapy.arping` for a single IP.
        ```bash
        python scapyarping.py
        ```
    *   `listnetworkscanner.py`: Scans a hardcoded subnet and prints results directly.
        ```bash
        python listnetworkscanner.py
        ```
    *   `networkscanner.py`: Scans a hardcoded subnet, collects results, then prints.
        ```bash
        python networkscanner.py
        ```

    **Important Note on Ethical Use:**
    Always replace `<target_ip_address_or_range>` or `<ip_address>` with an actual IP address or CIDR range you wish to scan. It is crucial to **only scan networks you own or have explicit, documented permission to test**. Unauthorized network scanning may be illegal and unethical. These tools are provided for educational and authorized penetration testing purposes only.
