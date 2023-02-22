# encoding: UTF-8
from decimal import *

getcontext().prec = 102

# Se calculan 2 dígitos más para no tener errores de aproximación
def sd(x):
    a = Decimal(x).sqrt().as_tuple().digits
    return sum(a) - a[-1] - a[-2]


# Para no tener errores en las raíces sin decimales
cuadrados = [i**2 for i in range(10)]
total = 0
for i in range(100):
    if i not in cuadrados:
        total += sd(i)
print(total)

"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
