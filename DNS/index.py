import socket

dominio = input("Alvo: ")
brute = ["ns1", "ns2", "ns3", "ns4", "www", "ftp", "intranet", "mail"]

for name in brute:
    DNS = name + "." + dominio
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass