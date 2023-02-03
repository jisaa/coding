grid = []
for _ in range(1000):
    grid.append([0] * 1000)

for line in open("inputs/day6.in"):
    words = line.split()
    x1, y1 = map(int, words[-3].split(","))
    x2, y2 = map(int, words[-1].split(","))
    if words[-4] == "on":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = 1
    if words[-4] == "off":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = 0
    if words[-4] == "toggle":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = 1 - grid[x][y]

total = sum(sum(r) for r in grid)
print("Part 1:", total)

grid = []
for _ in range(1000):
    grid.append([0] * 1000)

for line in open("inputs/day6.in"):
    words = line.split()
    x1, y1 = map(int, words[-3].split(","))
    x2, y2 = map(int, words[-1].split(","))
    if words[-4] == "on":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += 1
    if words[-4] == "off":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] -= 1
                if grid[x][y] < 0:
                    grid[x][y] = 0
    if words[-4] == "toggle":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += 2

total = sum(sum(r) for r in grid)
print("Part 2:", total)
