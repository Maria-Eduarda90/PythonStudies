def adiciona_na_lista(lista, f):
    return [f(x) for x in lista]

ints = [4, 0, 1, 3, 5]

adiciona_na_lista(ints, lambda x: x * 2)