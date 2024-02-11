import socket

host = input("Alvo: ")
ports = [21,22,80,443,445,3306,25]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    code = client.connect_ex((host, port))
    if code == 0:
        print(port, "OPEN")
