# encoding: UTF-8


def esPandigital(x):
    if x < 123456789 or 987654321 < x:
        return False
    c = [False, False, False, False, False, False, False, False, False]
    while x > 0:
        if c[x % 10 - 1]:
            return False
        c[x % 10 - 1] = True
        x //= 10
    for v in c:
        if not v:
            return False
    return True


a = 1
b = 1
k = 2

while not esPandigital(b % 1000000000) or not esPandigital(int(str(b)[:9])):
    a, b, k = b, a + b, k + 1
print("--->", k)
"""
The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.
It turns out that F(541), which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F(2749), which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that F(k) is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

"""
