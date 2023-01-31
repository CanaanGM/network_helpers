import scapy.all as sc

def scan(ip: str) -> dict[str, str]:
    """scans the network for available devices and captures thier IP and MAC
    and returns them in a dict

    Args:
        ip (str): IP range to scan 

    Returns:
        dict[str, str]: Ip as KEY : MAC as Value
    """

    arp = sc.ARP(pdst=ip)
    ether = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arp_ether = ether/arp
    answered_list, ignored_list = sc.srp(arp_ether, timeout=2, verbose=False)

    available_devices_info : dict = {
        # IP : MAC
    }

    for device in answered_list:
        available_devices_info[device.query.pdst] = device.answer.src
    
    return available_devices_info


def print_devices(devices: dict) -> None:
    """prints the IP : MAC for devices in a nice table

    Args:
        devices (dict): collection of devices
    """

    print("="*41) # header
    print("| Ip\t\tMAC Address\t\t|")
    print("| ------------------------------------- |")

    for ip,mac in devices.items():
        print (f"| {ip}\t{mac}       |")   
    print("="*41) # footer
 

user_ip = input("gimme an Ip range please and double check it there's no error handling here Q.Q: ")
if user_ip == "": user_ip = "192.168.1.1/24"
print_devices( scan(user_ip))