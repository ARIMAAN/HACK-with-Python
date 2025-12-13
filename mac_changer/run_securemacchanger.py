import subprocess
import argparse
import re

def get_arguments():
    # create an argument parser
    parser = argparse.ArgumentParser()
    # add an argument for the interface
    parser.add_argument("-i","--interface",dest='interface',help="Interface to change the mac address")
    # add an argument for the new mac address
    parser.add_argument("-m","--mac",dest='newmac',help="newmac address")
    # parse the arguments
    ops= parser.parse_args()
    # check if the interface argument was provided
    if not ops.interface:
            parser.error(" please specify a interface")
    # check if the new mac address argument was provided
    elif not ops.newmac:
        parser.error("Please specify a mac")
    # return the parsed arguments
    return ops

def change_mac(interface, new_mac):
    # bring the interface down
    subprocess.call(["ifconfig",interface,"down"])
    # change the mac address of the interface
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    # bring the interface back up
    subprocess.call(["ifconfig",interface,"up"])

def getcurentmac(interface):
    # run the ifconfig command and store the output
    ifconfig_result = subprocess.check_output(['ifconfig',interface])
    # decode the bytes output into a string
    ifconfig_result = ifconfig_result.decode('utf-8')
    # search for the mac address in the output
    mac_address_search=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    # if a mac address was found
    if mac_address_search:
        # return the found mac address
        return mac_address_search.group(0)
    else:
        # print an error message if no mac address was found
        print("couldnt get mac address")

# call the functions
ops = get_arguments()
interface= ops.interface
newmac= ops.newmac
oldmac =getcurentmac(interface)
print("Old mac is >"+str(oldmac))
change_mac(interface,newmac)
newmac= getcurentmac(interface)
print("New mac is  > "+str(newmac))