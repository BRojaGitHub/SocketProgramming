import socket

s = socket.socket()
# By default the TCP & IPV4 in bracket,
# if you want to use UDP or IPV6 mention it in bracket

print("Socket created")

s.bind(('localhost', 9999))
# You can use any of port number in between 0-65535

s.listen(3)  # 3 Clients are waiting to connect
print("Waiting for connection")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()

    print("Connected with ", addr)

    c.send(bytes("Welcome", 'utf-8'))
    # converts string into byte format
    c.close()
