def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
    return minimo

lista_teste = [2, 10, 3, 1, 4, 5]
menor = encontrar_minimo(lista_teste)
print(f"O menor elemento da lista é [{menor}]")

def somar_numeros_par(lista):
    soma = 0
    for elem in lista:
        if(elem % 2 == 0):
            soma += elem
    return soma

lista_teste = [2, 10, 3, 1, 4, 5]
soma = somar_numeros_par(lista_teste)
print(f"a soma é {soma}")