import socket

def ami_connect(port=5038):
    HOST = "127.0.0.1"
    USER = "pyclient"
    SECRET = "admin123"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, port))

    # Greeting
    greeting = s.recv(4096).decode()
    print("Greeting:", greeting)

    # Login
    login_msg = (
        f"Action: Login\r\n"
        f"Username: {USER}\r\n"
        f"Secret: {SECRET}\r\n"
        f"Events: off\r\n"
        f"\r\n"
    )
    s.sendall(login_msg.encode())

    response = s.recv(4096).decode()
    print("Login response:", response)

    if "Success" not in response:
        raise Exception("AMI login failed")

    return s
