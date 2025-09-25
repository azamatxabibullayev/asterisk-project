from utils import ami_connect, ami_logoff
import time

def make_call_play_announce():
    sock = ami_connect(port=5038)
    action = (
        "Action: Originate\r\n"
        "Channel: PJSIP/2000\r\n"        
        "Context: automation\r\n"       
        "Exten: play_2000\r\n"          
        "Priority: 1\r\n"
        "CallerID: Announce <1000>\r\n"
        "Async: true\r\n"
        "\r\n"
    )
    print("Sending Originate to play announce on 2000...")
    sock.sendall(action.encode())
    time.sleep(0.3)
    try:
        response = sock.recv(8192).decode(errors='ignore')
    except:
        response = ""
    print("Call response:", response.strip())


    time.sleep(0.5)
    ami_logoff(sock)

if __name__ == "__main__":
    make_call_play_announce()
