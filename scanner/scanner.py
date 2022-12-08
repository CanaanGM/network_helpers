import scapy.all as sc

def scan(ip):
    arp = sc.ARP(pdst=ip)
    ether = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    ## combine the request with the ether interface ? ? (look it up)
    arp_ether = ether/arp
    answered_list, ignored_list = sc.srp(arp_ether, timeout=2, verbose=False)

    available_devices_info : dict = {
        # IP : MAC
    }

    for device in answered_list:
        available_devices_info[device.query.pdst] = device.answer.src
    
    print("="*41) # header
    print("| Ip\t\tMAC Address\t\t|")

    for ip,mac in available_devices_info.items():
        print (f"| {ip}\t{mac}       |")   
    print("="*41) # footer
 

user_ip = input("gimme an Ip range please and double check it there's no error handling here Q.Q: ")
scan(user_ip)