# encoding: UTF-8

primos = [2, 3, 5, 7, 11, 13, 17, 19]


def esPrimo(x):
    global primos
    for p in primos:
        if x % p == 0:
            return False
        elif p**2 > x:
            return True
    return True


def _p(x):
    global primos
    while x > len(primos):
        i = primos[-1] + 2
        while not esPrimo(i):
            i += 2
        primos.append(i)
    return primos[x - 1]


def _r(x):
    p = _p(x)
    m = p**2
    a = x
    s1 = s2 = 1
    while a > 0:
        s1 = (s1 * (p - 1)) % m
        s2 = (s2 * (p + 1)) % m
        a -= 1
    return (s1 + s2) % m


max = 10**10
i = 7037
while _r(i) < max:
    i += 1
print("--->", i)

"""
Let p(n) be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (p(n)-1)^n + (p(n)+1)^n is divided by p(n)^2.

For example, when n = 3, p(3) = 5, and 4³ + 6³ = 280 = 5 mod 25.

The least value of n for which the remainder first exceeds 10⁹ is 7037.

Find the least value of n for which the remainder first exceeds 10¹⁰.
"""
