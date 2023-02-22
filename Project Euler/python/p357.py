"""
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""

# no need for primes over 10 000 for prime testing
primes = []
with open("primes.txt") as f:
    for line in f:
        p = int(line)
        if p > 20000:
            break
        primes.append(p)


def is_prime(x):
    for p in primes:
        if x % p == 0:
            return False
        if p * p > x:
            return True


total = 1
for n in range(2, 100000000, 2):
    if n % 1000000 == 0:
        print(n)
    if not (is_prime(n + 1)):
        continue
    complies = True
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            if not is_prime(d + n / d):
                complies = False
                break
    if complies:
        # print( n)
        total += n

print(total)
