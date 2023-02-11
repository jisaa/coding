"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

# using primes up to 10000 first
M = 10000
primes = []
with open("primes.txt") as f:
    for line in f:
        p = int(line)
        if p > M:
            break
        primes.append(p)


def is_prime(x):
    for p in primes:
        if x % p == 0:
            return False
        if p * p > x:
            return True


def can_concat(x, y):
    a = int(str(x) + str(y))
    b = int(str(y) + str(x))
    return is_prime(a) and is_prime(b)


N = len(primes)
for i in range(1, N):
    print("i:", i)
    a = primes[i]
    for j in range(i + 1, N):
        b = primes[j]
        if not can_concat(a, b):
            continue
        for k in range(j + 1, N):
            c = primes[k]
            if not can_concat(a, c) or not can_concat(b, c):
                continue
            for l in range(k + 1, N):
                d = primes[l]
                if not can_concat(a, d) or not can_concat(b, d) or not can_concat(c, d):
                    continue
                for m in range(l + 1, N):
                    e = primes[m]
                    pairs = [
                        # (a, b),
                        # (a, c),
                        # (a, d),
                        (a, e),
                        # (b, c),
                        # (b, d),
                        (b, e),
                        # (c, d),
                        (c, e),
                        (d, e),
                    ]

                    if all(can_concat(*pair) for pair in pairs):
                        print(a, b, c, d, e)
                        print(a + b + c + d + e)
                        exit()
