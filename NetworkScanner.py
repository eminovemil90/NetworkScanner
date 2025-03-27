import scapy.all as s
import optparse
def user_input():
    parser = optparse.OptionParser()
    parser.add_option("-i","--ip",dest="ip_address",help="ip addressini teyin etmeye komek edir")
    return parser.parse_args()

def check_input(ip_address):
    if not ip_address:
        ip_address=input("ip addressini daxil edin:")
    return ip_address

def network_scan(ip_address):
    arp_requst_packet=s.ARP(pdst=ip_address)###pdst -- destination address
    ####print(s.ls(s.ARP())) nece deyisiklik edeceyik ona baxiriq
    broadcast_packet=s.Ether(dst="ff:ff:ff:ff:ff:ff")#######dst ---- destination mac address
    full_packet=broadcast_packet/arp_requst_packet
    (answered,unanswered)= s.srp(full_packet, timeout=1)######timeout burda ipden cavab gelmese diger ipye kecmeye komek edir
    print(answered.summary())
print("""
  _   _      _                      _       _____                                 
 | \ | |    | |                    | |     / ____|                                
 |  \| | ___| |___      _____  _ __| | __ | (___   ___ __ _ _ __  _ __   ___ _ __ 
 | . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |\  |  __/ |_ \ V  V / (_) | |  |   <   ____) | (_| (_| | | | | | | |  __/ |   
 |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\ |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                                 by Emil Eminov

""")

#####alqoritmi: arp requstleri gondermek ucun scapy
### broadcast yayin
###birlesdirib respons almaq ucun
##### optparse
######son olaraq eger istifadeci -i --ip yazmasa


(user_input,args)=user_input()
ip_address=check_input(user_input.ip_address)
network_scan(ip_address)














