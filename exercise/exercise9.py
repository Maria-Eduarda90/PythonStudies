lista_numeros = [9.56876, 7.09476, 3.08437, 6.2398]

lista_precisao = [2, 2, 3, 3]

arredondamento = lambda x,y: round(x,y)

resultado = list(map(arredondamento, lista_numeros, lista_precisao))

print(resultado)