import sys, subprocess

def ip_reachable(ip_list:list[str]) -> None:
    """
    pings the IP to see if it is reachable
    """
    for ip in ip_list:
        ip = ip.rstrip("\n")
        ping_reply = subprocess.run(
            f"ping {ip} -n -c 2",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
            )
        if ping_reply.returncode > 0:
            print(f'\n{ip} not reachable, please double check. . .')
            sys.exit(1)
        else:
            print(f"\n{ip} reachable ~!\n")
