total = 0
chars = 0
expanded = 0
for line in open("inputs/day8.in"):
    line = line.strip()
    total += len(line)
    expanded += len(line) + 4

    line = line[1:-1]
    i = 0
    while i < len(line):
        chars += 1
        if line[i] == "\\":
            i += 1
            expanded += 1
            if line[i] == "x":
                i += 2
            else:
                expanded += 1
        i += 1

print("Part 1:", total - chars)
print("Part 2:", expanded - total)
