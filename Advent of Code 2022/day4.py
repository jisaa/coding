f = open("inputs/day4.in")

contained = overlap = 0
for line in f:
    line = line.strip()
    a, b = line.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    if a1 <= b1 and b2 <= a2 or b1 <= a1 and a2 <= b2:
        contained += 1
    if a1 <= b1 <= a2 or a1 <= b2 <= a2 or b1 <= a1 <= b2 or b1 <= a2 <= b1:
        overlap += 1
print("Part 1:", contained)
print("Part 2:", overlap)
