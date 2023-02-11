"""
Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same number of positive divisors.
For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""


def divisor_count(x):
    c = 2
    d = 2
    while d * d < x:
        if x % d == 0:
            c += 2
        d += 1
    if d * d == x:
        c += 1
    return c


total = 0
previous_count = 1

for n in range(2, 10**7):
    t = divisor_count(n)
    if t == previous_count:
        total += 1
    previous_count = t

    if n % 10000 == 0:
        print(n, total)

print(total)
