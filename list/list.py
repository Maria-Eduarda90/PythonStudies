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

for indice in range(0, len(equipments)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome...........: ", (equipments[indice]))
    print("Valor..........: ", (values[indice]))
    print("serial.........: ", (serials[indice]))
    print("Departamento...: ", (department[indice]))
