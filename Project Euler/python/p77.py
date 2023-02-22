"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

primes = []
with open("primes.txt") as f:
    for line in f:
        p = int(line)
        if p > 1000:
            break
        primes.append(p)


def nways_brute(x, partial_sum=[], sums=[]):
    if x == 0:
        t = tuple(sorted(partial_sum))
        if t in sums:
            return 0
        sums.append(t)
        return 1
    if x < 2:
        return 0
    n = 0
    for p in primes:
        if p < max(partial_sum + [0]):
            continue
        if p <= x:
            n += nways_brute(x - p, partial_sum + [p], sums)
        else:
            break
    return n


i = 0
t = nways_brute(i)
while t < 5000:
    i += 1
    t = nways_brute(i)
    print(i, t)
