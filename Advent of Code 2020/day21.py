ingredients = []
allergens = []
sa = set()
si = set()

for line in open("inputs/day21.in"):
    i, a = line.strip().split(" (contains ")
    ingredients.append(i.split())
    for i in ingredients[-1]:
        si.add(i)
    allergens.append(a[:-1].split(", "))
    for a in allergens[-1]:
        sa.add(a)

d = {a: si.copy() for a in sa}

done = []
for i in range(len(ingredients)):
    for a in allergens[i]:
        d[a] = d[a].intersection(set(ingredients[i]))
        if len(d[a]) == 1:
            done.append(a)

i = 0
while i < len(done):
    for a in sa:
        if a != done[i]:
            d[a] = d[a].difference(d[done[i]])
            if a not in done and len(d[a]) == 1:
                done.append(a)
    i += 1

safe = si.copy()
for a in d:
    safe = safe.difference(d[a])

total = 0
for i in ingredients:
    for s in safe:
        if s in i:
            total += 1
print("Part 1:", total)

print("Part 2:", ",".join(d[k].pop() for k in sorted(d.keys())))
