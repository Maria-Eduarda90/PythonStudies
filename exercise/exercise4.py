def eh_primo(n):
    if(n < 2):
        return False
    i = n // 2
    print(i)
    while(i > 1):
        if(n % i == 0):
            return False
        i = i - 1
    return True

def imprimir_resultado(numero, resultado):
    menssage = f'O número {numero} NÃO é primo'
    if(resultado):
        menssage = f'O número {numero} é primo'
    return menssage

numero = 7
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)