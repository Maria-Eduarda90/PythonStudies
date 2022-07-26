# o valor mediano é o valor no meio, depois  de classificar todos os valores

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x);

# se houver dois números no meio, divida a soma desses números por dois
# 77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103
# (86  + 87) / 2
