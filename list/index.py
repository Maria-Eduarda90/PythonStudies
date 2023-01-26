cart=[]
resp = "S"
while resp=="S":
    cart.append(input("Fruta: "))
    cart.append(input("Ferramenta: "))
    cart.append(input("Bebida: "))
    cart.append(float(input("Preço estimado a pagar: ")))
    resp = input("Digite \"s\" para continuar: ").upper()

print("")

for element in cart:
    print(element);