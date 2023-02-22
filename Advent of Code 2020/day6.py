totalAny = 0
totalAll = 0
current = ""
counter = {}
n = 0
for line in open("inputs/day6.in"):
    line = line.strip()
    if line:
        current += line
        for c in line:
            counter[c] = counter.get(c, 0) + 1
        n += 1
    else:
        totalAny += len(set(current))
        totalAll += len([k for k in counter if counter[k] == n])
        current = ""
        counter = {}
        n = 0

print("Part 1:", totalAny)
print("Part 2:", totalAll)
