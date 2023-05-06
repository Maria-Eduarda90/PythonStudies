list = [10, 2, 5, 7, 6, 3]
n = len(list)
soma = 0
for i in range(n):
    if(list[i]%2 == 0):
        soma += list[i]
print(f'o somatório dos elementos pares da lista é: {soma}')

soma = 0
for num in list:
    if(num%2 == 0):
        soma += num
print(f'o somatório dos elementos pares da lista é: {soma}')