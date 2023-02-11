n = 5


def sp(x, n):
    t = x
    s = 0
    while x:
        s += (x % 10) ** n
        x //= 10
    return t == s


def bound(x, n):
    return (9**n) * len(str(x))


m = 10
while m < bound(m, n):
    m *= 10

s = 0
for x in range(2, m):
    if sp(x, n):
        s += x
print(s)
