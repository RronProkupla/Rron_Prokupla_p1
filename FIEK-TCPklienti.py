import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Jepni IP: ")
port = int(input("Jepni portin: "))
s.connect((host, port))
while 1:
    print("\nType ? to show server commands.")

    var = input("Client>")
    if len(var)> 128:
        print("Kerkesa duhet te kete me pak se 128 karaktere!")
        s.close()
    else:
        s.send(str.encode(var))

    r = s.recv(1024).decode()
    print(r)

s.close()