num = int(input("Digite o numero de linhas: "))

for n in range(num):
    print(' '*(num-n), end='')

    print(' '.join(map(str, str(11**n))))