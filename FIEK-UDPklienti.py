import socket

HOST = input("Jepni IP: ")
PORT = int(input("Jepni portin: "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sever = (HOST, PORT)
print("\nType ? to show server commands.")
var = input("Client>")
if len(var) > 128:
    print("Kerkesa duhet te kete me pak se 128 karaktere!")
    s.close()
else:
    s.sendto(str.encode(var), sever)

r = s.recvfrom(1024)
message = r[0].decode()
print(message)
s.close()

