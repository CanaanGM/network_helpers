import sys 
from check_reachability import ip_reachable
from validate_ip_file import validate_file
from validate_ip import validate_ip
from ssh_connection import ssh_connection
from thread_handler import create_threads

ip_list = validate_file()
try:
    validate_ip(ip_list)
    ip_reachable(ip_list)
    create_threads(ip_list, ssh_connection)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

