def rc(code):
    s = ""
    for i in code[:-3]:
        if i == "B":
            s += "1"
        else:
            s += "0"
    r = int(s, 2)
    s = ""
    for i in code[-3:]:
        if i == "R":
            s += "1"
        else:
            s += "0"
    c = int(s, 2)
    return r, c


def id(r, c):
    return r * 8 + c


seen = []
for line in open("inputs/day5.in"):
    r, c = rc(line.strip())
    seen += (id(r, c),)
seen.sort()
print("Part 1:", seen[-1])

for i in range(len(seen)):
    if seen[i] + 1 != seen[i + 1]:
        print("Part 2:", seen[i] + 1)
        break
