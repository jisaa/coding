f = open("p24.in")

grid = []
for line in f.readlines():
    grid.append(line.strip())

storms = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in "><^v":
            storms.append((i - 1, j - 1, grid[i][j]))

end_a, end_b = len(grid) - 1, len(grid[-1]) - 1


def are_storms_at(i, j, time):
    wind = {
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
        "^": (-1, 0),
    }
    for a, b, dir in storms:
        da, db = wind[dir]
        x = (a + da * time) % len(grid)
        y = (b + db * time) % len(grid[x])
        if x == i and y == j:
            return True
    return False


# pos_i, pos_j, time
q = [(-1, 0, 0)]
vueltas = 0
while 1:
    q.sort(key=lambda x: x[0] + x[1])
    print(len(q), max(t[-1] for t in q), vueltas)
    vueltas += 1
    a, b, time = q.pop()
    # can exit
    if a == len(grid) - 1 and b == len(grid[0]) - 1:
        print("Part 1:", time + 1)
        break
    # can stay
    if not are_storms_at(a, b, time + 1):
        q.append((a, b, time + 1))
    # can move right
    if b + 1 < len(grid[a]) and not are_storms_at(a, b + 1, time + 1):
        q.append((a, b + 1, time + 1))
    # can move left
    if b - 1 >= 0 and not are_storms_at(a, b - 1, time + 1):
        q.append((a, b - 1, time + 1))
    # can move down
    if a + 1 < len(grid) and not are_storms_at(a + 1, b, time + 1):
        q.append((a + 1, b, time + 1))
    # can move up
    if a - 1 >= 0 and not are_storms_at(a - 1, b, time + 1):
        q.append((a - 1, b, time + 1))

# 327 too low
