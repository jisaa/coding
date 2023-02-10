from collections import Counter

steps = 40

f = open("inputs/day14.in")
string = f.readline().strip()
f.readline()

replacements = {}
for line in f:
    x = line.strip()
    a, b = x.split(" -> ")
    replacements[a] = b


def expand(pair, steps, replacements, mem={}):
    if (pair, steps) not in mem:
        a, b = pair
        if steps == 0:
            mem[(pair, steps)] = Counter(pair)
        else:
            x = replacements[pair]
            f1 = expand(a + x, steps - 1, replacements)
            f2 = expand(x + b, steps - 1, replacements)
            mem[(pair, steps)] = f1 + f2 - Counter(x)
    return mem[(pair, steps)]


freqs = Counter({string[0]: 1})
for i in range(len(string) - 1):
    pair = string[i : i + 2]
    fs = expand(pair, steps, replacements)
    freqs = freqs + fs - Counter(pair[0])

vals = freqs.values()
print(max(vals) - min(vals))
