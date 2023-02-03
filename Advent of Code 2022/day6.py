s = open("inputs/day6.in").readline().strip()

i = 0
while len(set(s[i : i + 4])) < 4:
    i += 1
print("Part 1", i + 4)


i = 0
while len(set(s[i : i + 14])) < 14:
    i += 1
print("Part 1", i + 14)
