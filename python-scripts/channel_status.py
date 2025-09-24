from utils import ami_connect, ami_command, ami_logoff

def get_channels():
    sock = ami_connect()
    response = ami_command(sock, "core show channels")
    print(response)
    ami_logoff(sock)


if __name__ == "__main__":
    get_channels()
