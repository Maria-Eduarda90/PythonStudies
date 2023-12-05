import re

estados = [' alabama ', 'Georgia!', 'Georgia', 'georgia', 'Florida', 'south carolina##', ' west virginia?']

def limpar_funcao(strings):
    result = []
    for valor in strings:
        valor = valor.strip()
        valor = re.sub('[!#?]', '', valor)
        valor = valor.title()
        result.append(valor)

    return result

print(limpar_funcao(estados))