# coding: utf-8

"""
Given is the function f(x) = ⌊2^(30.403243784-x^2)⌋ × 10^(-9) ( ⌊ ⌋ is the floor-function),
the sequence u_n is defined by u_0 = -1 and u_(n+1) = f(u_n).

Find u_n + u_(n+1) for n = 10^12.
Give your answer with 9 digits after the decimal point.
"""


def f(x):
    return int(2 ** (30.403243784 - x**2)) * 10 ** (-9)


# no need to check them all, it converges early
a = -1
for n in range(1000):
    print(n, a, a + f(a))
    a = f(a)
