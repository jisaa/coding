line = open("inputs/day1.in").readline().strip()

level = 0
i = 1
first = -1
for c in line:
    if c == "(":
        level += 1
    else:
        level -= 1
        if level < 0 and first == -1:
            first = i
    i += 1

print("Part 1:", level)
print("Part 2:", first)
