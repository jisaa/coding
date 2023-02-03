def priority(c):
    if "a" <= c <= "z":
        return ord(c) - ord("a") + 1
    return ord(c) - ord("A") + 27


total = 0
f = open("inputs/day3.in")
for line in f:
    line = line.strip()
    l = len(line)
    left = line[: l // 2]
    right = line[l // 2 :]
    in_both = set(left).intersection(set(right)).pop()
    total += priority(in_both)
print("Part 1:", total)

total = i = 0
f = open("inputs/day3.in")
lines = f.readlines()
while i < len(lines):
    in_all = (
        set(lines[i].strip())
        .intersection(set(lines[i + 1].strip()))
        .intersection(set(lines[i + 2].strip()))
        .pop()
    )
    total += priority(in_all)
    i += 3
print("Part 2:", total)
