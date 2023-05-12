valores = input("Digite mais de três numeros e dê um espaço entre eles: ")

valores = [int(i) for i in valores.split()]

def altera_lista(lista):
    lista[2] = lista[2] + 10
    return lista

def main():
    print("Nova lista", altera_lista(valores))
    print("Nova lista", altera_lista(valores))

if __name__ == "__main__":
    main()