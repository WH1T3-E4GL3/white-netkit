from netkitfun import *

os.system("clear")
os.system("figlet White Netkit | lolcat")
message = "    Developed By WHITE L'            The Network Kit"
# Use subprocess to execute the echo command and pipe the message to lolcat
p1 = subprocess.Popen(['echo', '-n', message], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['lolcat'], stdin=p1.stdout, stdout=subprocess.PIPE)
# Decode the output and print it
output = p2.communicate()[0].decode('utf-8')
print(output)


message = """\033[33m
        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        █              𝗠𝗘𝗡𝗨
        █=============================================
        █ 1.  Change MAC address                                      
        █ 2.  Reset MAC address                                     
        █ 3.  Route your full device through TOR
        █ 4.  Stop routing via TOR
        █ 5.  show devices connected to the Network
        █ 6.  Start a deauthentication attack
        █ 7.  Start ARP Poisoning attack
        █ 8.  Sniff the http traffic in the network
        █ 9.  Dos attack (UDP flooding)
        █ 10. Scan your ip range for showing active devices
        █ 11. Contact devoloper
        █ 12. Exit
        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
\033[0m
"""
print(message)

choice = int(input("\033[1m\033[33;32m[+] Select an option number from the above menu >\033[0m "))

if choice == 1:
    macchanger()
elif choice == 2:
    resetmac()
elif choice == 3:
    torroute()
elif choice == 4:
    torstop()
elif choice == 5:
    show_devices()
elif choice == 6:
    deauth()
elif choice == 7:
    arp_spoof_main()
elif choice == 8:
    sniff_http_traffic()
elif choice == 9:
    udp_flood_attack()
elif choice == 10:
    iprange=input("[+] Enter your ip start range(eg:10.0.2.0) > ")
    scan_network(iprange)
elif choice == 11:
    os.system("clear")
    print("""
    \033[32m================================================================\033[0m
    \033[32mTool devoloped  : WHITE L'\033[0m
    \033[33mGithub 	    : https://github.com/WH1T3-E4GL3/\033[0m
    \033[33mTelegram        : https://t.me/Ka_KsHi_HaTaKe\033[0m
    \033[32m================================================================\033[0m
    """)
elif choice == 12:
    print(" ")
    print("Ok bye...")
    print("Thank you for using white netkit...")
    print(" ")
    os.system("exit")
elif choice == 13:
    # Prompt user for network interface name
    ifname = input("Enter the network interface name: ")
    show_devices(ifname)
else:
    print("\033[31m[ERROR!]\033[0m Invalid input, please try again.")
