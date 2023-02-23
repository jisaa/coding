f = open("inputs/day24.in")

grid = []
for line in f.readlines():
    grid.append(line.strip()[1:-1])
grid = grid[1:-1]

storms = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in "><^v":
            storms.append((i, j, grid[i][j]))


def are_storms_at(i, j, storms, time):
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


# Takes about 6 minutes to finish
# pos_i, pos_j, time
q = [(-1, 0, 0)]
best_time = 9999
seen = set(q)
while q:
    # try the position closest to the exit (Manhattan distance)
    q.sort(key=lambda x: x[0] + x[1])
    a, b, time = q.pop()
    # can exit
    if a == len(grid) - 1 and b == len(grid[0]) - 1:
        if time + 1 < best_time:
            best_time = time + 1
            q = [t for t in q if t[2] < best_time]
    # check all directions, including current position
    for da, db in ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)):
        x = a + da
        y = b + db
        if (
            0 <= x < len(grid)
            and 0 <= y < len(grid[x])
            and not are_storms_at(x, y, storms, time + 1)
            and (x, y, time + 1) not in seen
            and time + 1 < best_time
        ):
            seen.add((x, y, time + 1))
            q.append((x, y, time + 1))

print("Part 1:", best_time)
