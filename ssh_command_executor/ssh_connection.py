import paramiko, os.path, time, sys, re

user_creds_file = input(r"\nFile path; c:\user\file.txt ")

if not os.path.isfile(user_creds_file):
    print(f"\nFile {user_creds_file} doesn't exist. . . \n")
    sys.exit(1)    

commads_file = input("\nCommand file path: ")
if not os.path.isfile(commads_file):
    print(f"\nCommand file {commads_file} doesn't exist. . .\n")
    sys.exit(1)


def ssh_connection(ip):
    """
    conects to the IP and tries to execute the commands
    """
    session = paramiko.SSHClient()
    try:
        # a line is like dis -> user,thing
        with open(user_creds_file, mode="rt") as user_file:
            for line in user_file:
                username, password = line.split(",")

                session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                session.connect(ip, username=username, password=password)

                connection = session.invoke_shell()

                connection.send("enable\n")
                connection.send("terminal length 0\n")
                time.sleep(1)

                connection.send("\n")
                connection.send("configure terminal\n")
                time.sleep(1)

                # open the command file to start using them
                with open(commads_file, mode="rt") as cmd_file:
                    for line in cmd_file:
                        connection.send(f"{line}\n")
                        time.sleep(2)

                router_output = connection.recv(65535)
                if re.search(b"% Invalid input", router_output):
                    print(f"Error encountered in device: {ip}")
                else:
                    print(f"\nDone for device: {ip}.\n")

    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")
        session.close()
        sys.exit(1)   
    except Exception as ex:
        print(f"An Error has Occu'd: {ex.message}\nWhy:{ex.__cause__}\n{ex}")
        session.close()
        sys.exit(1)