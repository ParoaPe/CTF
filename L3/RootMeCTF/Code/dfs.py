import socket

hostname = "ctf10k.root-me.org"
port = 8001

def netcat(hostname, port, content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))

    sock.sendall(content)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()
    
    print(res)

    print("Connection closed.")
    sock.close

content = "yes"

netcat(hostname, port, content)