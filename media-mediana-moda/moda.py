# O valor Modo é o valor que aparece o maior número de vezes:

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)