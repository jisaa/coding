"""
Let p(n) represent the number of different ways in which n coins can be separated into piles.
For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""


values = {0: 1, 1: 1, 2: 2}


def p(n):
    global values
    if n < 0:
        return 0
    if n in values:
        return values[n]

    t = 0
    m = 1
    a = m * (3 * m - 1) / 2
    b = -m * (-3 * m - 1) / 2
    while a <= n or b <= n:
        # print(n, m, a, b)
        s = (-1) ** (abs(m) - 1)
        t += s * p(n - a) + s * p(n - b)
        m += 1
        a = m * (3 * m - 1) / 2
        b = -m * (-3 * m - 1) / 2
    values[n] = t
    return t


x = 1
while p(x) % 1000000 != 0:
    x += 1
    if x % 10000 == 0:
        print(x)
print(x)
