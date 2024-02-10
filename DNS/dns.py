import socket
import os

diretorio = os.getcwd()
dominio = input("Alvo: ")
txt = diretorio + "\\DNS\\bruteforce.txt"

try:
    with open(txt, "r") as arquivo:
        bruteforce = arquivo.readlines()

    
    for name in bruteforce:
        DNS = name.strip("\n") + "." + dominio
        try:
            print(DNS + ": " + socket.gethostbyname(DNS))
        except socket.gaierror:
            pass

except FileNotFoundError:
    print("Não encontrado")