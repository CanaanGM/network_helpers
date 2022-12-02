import paramiko, os.path, time, sys, re

user_creds_file = input("\nUser creds file path: ")
# debugging
if user_creds_file == "":
    user_creds_file = "./ssh_command_executor/user_creds.txt"

if not os.path.isfile(user_creds_file):
    print(f"\nFile {user_creds_file} doesn't exist. . . \n")
    sys.exit(1)

commads_file = input("\nCommand file path: ")
# debugging
if commads_file == "":
    commads_file = "./ssh_command_executor/commands.txt"

if not os.path.isfile(commads_file):
    print(f"\nCommand file {commads_file} doesn't exist. . .\n")
    sys.exit(1)


def ssh_connection(ip):
    """
    conects to the IP and tries to execute the commands
    using 'exec_command' will work for simple commands
    to install stuff u need to open a terminal session
    """
    client = paramiko.SSHClient()

    try:
        # a line is like dis -> user,thing
        with open(user_creds_file, mode="rt") as user_file:
            for cred_line in user_file:
                username, password = cred_line.split(",")

                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip.rstrip("\n"), username=username, password=password)

                connection = client.invoke_shell()

                """
                send    -> 
                recieve <-
                something is missing here
                     
                """

                # open the command file to start using them

                with open(commads_file, mode="rt") as cmd_file:
                    lines = cmd_file.readlines()
                    line_count = len(lines)
                    while line_count > 0 :
                        
                        connection.send("\n")
                        recieved = connection.recv(4096)
                        print(recieved)
                        
                        if "working" in recieved.decode():
                            continue 

                        for cmd in lines:
                            connection.send(cmd)
                            if "password for" in recieved.decode() or "sudo" in cmd:
                                connection.send(f"{password}\n")
                                print(connection.recv(4096))
                                time.sleep(20) # to give the server time to install
                            line_count -= 1

                router_output = connection.recv(65535)
                if re.search(b"% Invalid input", router_output):
                    print(f"Error encountered in device: {ip}")
                else:
                    print(f"\nDone for device: {ip}.\n")

    except paramiko.AuthenticationException:
        print(
            "* Invalid username or password :( \n* Please check the username/password file or the device configuration."
        )
        print("* Closing program... Bye!")
        sys.exit()
    except Exception as ex:
        print(f"An Error has Occu'd: {ex}\nWhy:{ex.__cause__}")
        sys.exit()
    finally:
        client.close()


#  import paramiko as pm
#  ip = '192.168.88.129'
#  session = pm.SSHClient()
#  session.set_missing_host_key_policy(pm.AutoAddPolicy())
#  session.connect(ip, username='saturn', password='saturn')
#  connection = session.invoke_shell()
#  print(connection.recv(4096))
