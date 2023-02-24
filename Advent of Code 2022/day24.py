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


# Takes about 3 minutes to finish
def get_best_time(storms, max_x, max_y, from_i, from_j, to_i, to_j, start_time=0):
    # pos_i, pos_j, time
    q = [(from_i, from_j, start_time)]
    best_time = 9999
    seen = set(q)
    while q:
        # try the position closest to the exit (Manhattan distance)
        q.sort(key=lambda x: abs(to_i - x[0]) + abs(to_j - x[1]))
        a, b, time = q.pop(0)
        # can exit
        if a == to_i and b == to_j:
            if time + 1 < best_time:
                best_time = time + 1
                print(best_time)
                q = [t for t in q if t[2] < best_time]
        # check all directions, including current position
        for da, db in ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)):
            x = a + da
            y = b + db
            if (
                0 <= x < max_x
                and 0 <= y < max_y
                and abs(x - to_i) + abs(y - to_j) < best_time - time
                and time + 1 < best_time
                and (x, y, time + 1) not in seen
                and not are_storms_at(x, y, storms, time + 1)
            ):
                seen.add((x, y, time + 1))
                q.append((x, y, time + 1))
    return best_time


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

part_1_time = get_best_time(
    storms,
    len(grid),
    len(grid[0]),
    -1,
    0,
    len(grid) - 1,
    len(grid[0]) - 1,
)
print("Part 1:", part_1_time)

back_to_start_time = get_best_time(
    storms,
    len(grid),
    len(grid[0]),
    len(grid),
    len(grid[0]) - 1,
    0,
    0,
    part_1_time,
)
print("Back to start:", back_to_start_time)
final_time = get_best_time(
    storms,
    len(grid),
    len(grid[0]),
    -1,
    0,
    len(grid) - 1,
    len(grid[0]) - 1,
    back_to_start_time,
)

print("Part 2:", final_time)
