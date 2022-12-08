import scapy.all as sc

def scan(ip):
    ar_request = sc.ARP(pdst=ip)
    # pprint.pprint(dir(ar_request))
    # print(ar_request.summary())

    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    # sc.ls(broadcast)
    # print(broadcast.summary())

    arp_req_broadcast = broadcast/ar_request
    # print(arp_req_broadcast.summary())
    # print(arp_req_broadcast.show())
    answerd_list, unanswerd_list = sc.srp(arp_req_broadcast, timeout=1, verbose=False)

    # can make a dict or a list[Tuples] to hold the values

    utilized_ip_mac : dict = {}

    print("="*41)
    for thing in answerd_list:
        utilized_ip_mac[thing.query.pdst] = thing.answer.src
       
    print("| Ip\t\tMAC Address\t\t|")
    print("-"*41)
    for ip,mac in utilized_ip_mac.items():
        print (f"| {ip}\t{mac}       |")
        # print("|\t \t\t\t\t|")
    print("="*41)
    

scan('192.168.1.1/24')

def old_print():
    for thing in answerd_list:
        # print(dir(thing))
        # print("="*89)
        # print(dir(thing.answer))
        # print("="*89)

        # print(thing[0])
        # print("="*89)

        # print(thing.answer.summary())
        
        # print("="*89)
        # print(thing.answer.dst) # MY MAC adress
        # print(thing.answer.src) # Target Mac Adress
        # # print(thing.answer.display()) # gives information 

        # # print(thing.answer.sent_time) 
        # # print(thing.answer.src) # Target Mac Adress
        
        
        # print("="*89)


        print(f"target IP: {thing.query.pdst}")
        print(f"target MAC: {thing.answer.src}")
        print(f"target Name: {None}")

        print("="*89)