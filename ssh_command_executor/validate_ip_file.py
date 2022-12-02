import os.path, sys

def validate_file() -> list[str]:
    """
    checks if the file exists or not, 
    if it does, it extracts the IPs and returns them as a 
    >> list[str]
    """

    ip_file = input("\nIp file path: ")
    if ip_file == '': ip_file = "./ssh_command_executor/ip_file.txt"
    if os.path.isfile(ip_file):
        print("\nFile exsits, extracting IPs\n")
    else:
        print("\nFile not found, please check then try again.\n ")
        sys.exit(1)
    ip_list :list[str] = []
    with open(ip_file, mode="rt") as file:
        for ip in file:
            ip_list.append(ip)

    return ip_list
