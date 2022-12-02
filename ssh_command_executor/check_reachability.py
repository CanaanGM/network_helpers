import sys, subprocess

def ip_reachable(ip_list:list[str]) -> None:
    for ip in ip_list:
        ping_reply = subprocess.call(
            f"ping {ip} -n 2",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if ping_reply > 0:
            print(f'\n{ip} not reachable, please double check. . .')
        else:
            print(f"\n{ip} reachable ~!\n")
