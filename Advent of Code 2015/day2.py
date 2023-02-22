paper = 0
ribbon = 0

for line in open("inputs/day2.in"):
    line = line.strip()
    a, b, c = map(int, line.split("x"))
    paper += 2 * (a * b + b * c + a * c) + min(a * b, b * c, a * c)
    ribbon += 2 * (a + b + c - max(a, b, c)) + a * b * c


print("Part 1:", paper)
print("Part 2:", ribbon)
