import socket
import time

HOST = "127.0.0.1"
AMI_USER = "pyclient"
AMI_SECRET = "admin123"


def ami_connect(port=5038, timeout=5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((HOST, port))

    greeting = s.recv(4096).decode(errors='ignore')
    print("Greeting:", greeting.strip())

    login_msg = (
        f"Action: Login\r\n"
        f"Username: {AMI_USER}\r\n"
        f"Secret: {AMI_SECRET}\r\n"
        f"Events: off\r\n"
        f"\r\n"
    )
    s.sendall(login_msg.encode())
    response = s.recv(4096).decode(errors='ignore')
    print("Login response:", response.strip())

    if "Success" not in response:
        raise Exception("AMI login failed: " + response)

    return s


def ami_command(sock, command, wait=0.1):
    if not sock:
        raise ValueError("Socket not connected")
    sock.sendall((command + "\r\n\r\n").encode())
    time.sleep(wait)
    try:
        data = sock.recv(16384).decode(errors='ignore')
    except socket.timeout:
        data = ""
    return data


def ami_logoff(sock):
    if not sock:
        return
    try:
        sock.sendall("Action: Logoff\r\n\r\n".encode())
        time.sleep(0.1)
        try:
            _ = sock.recv(4096)
        except:
            pass
        sock.close()
    except:
        pass
