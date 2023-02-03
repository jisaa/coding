cities = set()

for line in open("inputs/day9.in"):
    a, _, b, __, d = line.split()
    cities.add(a)
    cities.add(b)

distances = []
for _ in range(len(cities)):
    distances.append([0] * len(cities))

cities = sorted(cities)
for line in open("inputs/day9.in"):
    a, _, b, __, d = line.split()
    i = cities.index(a)
    j = cities.index(b)
    distances[i][j] = distances[j][i] = int(d)

from itertools import permutations

best = sum(sum(r) for r in distances)
worst = 0

for order in list(permutations(range(len(cities)))):
    t = 0
    for i in range(1, len(order)):
        t += distances[order[i]][order[i - 1]]
    best = min(best, t)
    worst = max(worst, t)

print("Part 1:", best)
print("Part 2:", worst)
