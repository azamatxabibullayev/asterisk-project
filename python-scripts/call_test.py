from utils import ami_connect

def make_call():
    sock = ami_connect(port=5038)
    action = (
        "Action: Originate\r\n"
        "Channel: SIP/1000\r\n"      
        "Exten: 2000\r\n"            
        "Context: default\r\n"       
        "Priority: 1\r\n"
        "CallerID: 1000\r\n"
        "Async: true\r\n\r\n"
    )
    sock.sendall(action.encode())
    response = sock.recv(4096).decode()
    print("Call response:", response)

if __name__ == "__main__":
    make_call()
