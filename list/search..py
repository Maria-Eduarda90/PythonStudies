equipments=[]
values=[]
serials=[]
department=[]

resp = "S"

while resp =="S":
    equipments.append(input("Equipamento: "))
    values.append(float(input("Valor: ")))
    serials.append(int(input("Número serial: ")))
    department.append(input("Departamento: "))
    resp = input("Digite \"s\" para continuar: ").upper()

search = input("\nDigite o nome do equipamento que deseja buscar: ")

print("")

for indice in range(0, len(equipments)):
    if search == equipments[indice]:
        print("Valor........: ", (values[indice]))
        print("serial.......: ", (serials[indice]))