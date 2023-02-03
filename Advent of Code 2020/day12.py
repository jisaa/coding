x = y = 0
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
di = 0
s = set()
for line in open("inputs/day12.in"):
    d = int(line[1:])
    if line[0] == "N":
        y += d
    if line[0] == "S":
        y -= d
    if line[0] == "E":
        x += d
    if line[0] == "W":
        x -= d
    if line[0] == "L":
        di += d // 90
        di %= 4
    if line[0] == "R":
        di -= d // 90
        di %= 4
    if line[0] == "F":
        x += dirs[di][0] * d
        y += dirs[di][1] * d

print("Part 1:", abs(x) + abs(y))

wx = 10
wy = 1
x = y = 0
s = set()
for line in open("inputs/day12.in"):
    d = int(line[1:])
    if line[0] == "N":
        wy += d
    if line[0] == "S":
        wy -= d
    if line[0] == "E":
        wx += d
    if line[0] == "W":
        wx -= d
    if line[0] == "L":
        d //= 90
        while d:
            wx, wy = -wy, wx
            d -= 1
    if line[0] == "R":
        d //= 90
        while d:
            wx, wy = wy, -wx
            d -= 1
    if line[0] == "F":
        x += wx * d
        y += wy * d

print("Part 2:", abs(x) + abs(y))
