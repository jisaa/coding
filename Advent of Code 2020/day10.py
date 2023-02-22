a = list(map(int, open("inputs/day10.in")))
a.sort()
a = [0] + a + [a[-1] + 3]

d1 = 0
d3 = 0

for i in range(1, len(a)):
    if a[i] - a[i - 1] == 1:
        d1 += 1
    if a[i] - a[i - 1] == 3:
        d3 += 1

print("Part 1:", d1 * d3)

options = [1] * len(a)

for i in range(len(a) - 2, -1, -1):
    options[i] = options[i + 1]
    if i + 2 < len(a) and a[i + 2] - a[i] < 4:
        options[i] += options[i + 2]
    if i + 3 < len(a) and a[i + 3] - a[i] < 4:
        options[i] += options[i + 3]

print("Part 2:", options[0])
