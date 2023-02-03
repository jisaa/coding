replacements = {}
start = ""
for line in open("inputs/day19.in"):
    line = line.strip()
    if " => " in line:
        a, b = line.split(" => ")
        if a not in replacements:
            replacements[a] = []
        replacements[a].append(b)
    else:
        start = line

new_molecules = set()
for i in range(len(start)):
    for k in replacements:
        if k == start[i : i + len(k)]:
            for b in replacements[k]:
                t = start[:i] + b + start[i + len(k) :]
                new_molecules.add(t)

print("Part 1:", len(new_molecules))