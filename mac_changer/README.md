# Secure MAC Changer

This Python script allows you to easily change the MAC (Media Access Control) address of a specified network interface on your system. It's a useful tool for privacy, testing, or other network-related tasks.

## How It Works

The script utilizes `ifconfig` commands to bring down the specified network interface, change its MAC address, and then bring it back up. It also verifies the MAC address before and after the change.

## Prerequisites

*   **Python 3**: Ensure you have Python 3 installed.
*   **Linux-based OS**: This script is designed for Linux systems as it relies on the `ifconfig` utility.
*   **Root Privileges**: The script requires root privileges to modify network interface settings.

## Usage

To run the script, you need to provide the network interface you want to modify and the new MAC address you wish to set.

```bash
sudo python3 run_securemacchanger.py -i <INTERFACE_NAME> -m <NEW_MAC_ADDRESS>
```

### Arguments:

*   `-i` or `--interface`: Specifies the network interface (e.g., `eth0`, `wlan0`).
*   `-m` or `--mac`: Specifies the new MAC address in the format `XX:XX:XX:XX:XX:XX`.

### Example:

To change the MAC address of `wlan0` to `00:11:22:33:44:55`:

```bash
sudo python3 run_securemacchanger.py -i wlan0 -m 00:11:22:33:44:55
```

The script will output the old MAC address and the newly set MAC address for verification.
