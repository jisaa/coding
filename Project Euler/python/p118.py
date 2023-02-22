"""
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers,
different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
"""

from itertools import permutations

# biggest number is 987654321, need sqrt(987654321)=31427 as max prime for primality test
primes = []
with open("primes.txt") as f:
    for line in f:
        p = int(line)
        if p > 31427:
            break
        primes.append(p)


def is_prime(n):
    if n < 2:
        return False
    for p in primes:
        if p * p > n:
            return True
        if n % p == 0:
            return False


def prime_partitions(w, others=[]):
    if not w:
        yield others
    a = 1
    while a <= len(w):
        if is_prime(int(w[:a])):
            for i in prime_partitions(w[a:], others + [w[:a]]):
                yield i
        a += 1
    return


# takes about 10 seconds
p = permutations("123456789")
seen = set()
for s in p:
    # no primes can end in 4, 6 or 8
    # there could be a split that ends in 2 or 5,
    # but those would be counted when the 2 or 5 is at the start instead of the end
    if s[-1] in "24685":
        continue

    s = "".join(s)
    for p in prime_partitions(s):
        t = tuple(sorted(p))
        seen.add(t)

print(len(seen))
