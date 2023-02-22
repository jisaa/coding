from itertools import permutations


def arrangement_happiness(arrangement, happiness):
    t = 0
    for i in range(len(arrangement)):
        t += happiness[arrangement[i]][arrangement[i - 1]]
        t += happiness[arrangement[i]][arrangement[(i + 1) % len(happiness)]]
    return t


lines = open("inputs/day13.in").readlines()
names = sorted(set([line.split()[0] for line in lines]))

happiness = []
for _ in names:
    happiness.append([0] * len(names))

for line in lines:
    words = line.split()
    a = words[0]
    b = words[-1][:-1]
    v = int(words[3])
    if words[2] == "lose":
        v *= -1
    happiness[names.index(a)][names.index(b)] = v

best = -99999
for order in permutations(range(len(names))):
    best = max(best, arrangement_happiness(order, happiness))

print("Part 1:", best)

# add myself to the input set
for row in happiness:
    row.append(0)
happiness.append([0] * (len(names) + 1))

# recalculate
best = -99999
for order in permutations(range(len(names) + 1)):
    best = max(best, arrangement_happiness(order, happiness))

print("Part 2:", best)
