f = open("inputs/day1.in")

cur = 0
loads = []
for line in f:
    line = line.strip()
    if line:
        cur += int(line)
    else:
        loads.append(cur)
        cur = 0
loads.append(cur)
loads.sort()
print("Part 1:", loads[-1])
print("Part 2:", sum(loads[-3:]))
