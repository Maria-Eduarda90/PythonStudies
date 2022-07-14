nome = str(input("Digite o nome do aluno: "))
numero1 = int(input("digite a nota 1: "))
numero2 = int(input("digite a nota 2: "))

media = (numero1 + numero2) / 2

if media >= 6:
    print(f'{nome}, voçê foi aprovado(a)!')
elif media < 6 and media >= 4:
    print(f'{nome} voçê ficou de recuperação!')
else:
    print(f'{nome} voçê reprovou :(')