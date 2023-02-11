primes = [2, 3, 5, 7]


def is_prime(x):
    global primes
    for p in primes:
        if x % p == 0:
            return False
        if p * p > x:
            break
    primes.append(x)
    return True


with open("primes.txt", "w") as out:
    out.write("2")
    out.write("\n")
    for i in range(3, 10**8, 2):
        if is_prime(i):
            out.write(str(i))
            out.write("\n")
