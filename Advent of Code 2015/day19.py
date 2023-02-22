replacements = {}
for line in open("inputs/day19.in"):
    line = line.strip()
    if " => " in line:
        a, b = line.split(" => ")
        if a not in replacements:
            replacements[a] = []
        replacements[a].append(b)
    else:
        medicine = line


def distinct_replacements(start, replacements):
    new_molecules = set()
    for i in range(len(start)):
        for k in replacements:
            if k == start[i : i + len(k)]:
                for b in replacements[k]:
                    t = start[:i] + b + start[i + len(k) :]
                    new_molecules.add(t)
    return new_molecules


print("Part 1:", len(distinct_replacements(medicine, replacements)))

# start from medicine, apply replacements backwards, end up with "e"
q = [(0, medicine)]
seen = set()

reverse = {}
for k in replacements:
    for v in replacements[k]:
        reverse[v] = [k]

q = [(0, medicine)]
seen = set()
seen.add(medicine)
while q:
    # pick shortest molecule available
    q.sort(key=lambda i: len(i[1]))
    steps, molecule = q.pop(0)
    for mutation in distinct_replacements(molecule, reverse):
        if mutation == "e":
            print("Part 2:", steps + 1)
            exit()
        if mutation not in seen:
            q.append((steps + 1, mutation))
            seen.add(mutation)
