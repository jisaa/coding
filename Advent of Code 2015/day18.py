grid = []
for line in open("inputs/day18.in"):
    grid.append(list(line.strip()))

for _ in range(100):
    new_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[i])):
            n = 0
            for di, dj in (
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ):
                x = i + di
                y = j + dj
                n += 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == "#"

            if grid[i][j] == "#":
                if n in [2, 3]:
                    new_row.append("#")
                else:
                    new_row.append(".")
            else:
                if n == 3:
                    new_row.append("#")
                else:
                    new_row.append(".")
        new_grid.append(new_row)
    grid = new_grid

total = 0
for row in grid:
    for i in row:
        total += i == "#"

print("Part 1:", total)


grid = []
for line in open("inputs/day18.in"):
    grid.append(list(line.strip()))

for _ in range(100):
    new_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[i])):
            n = 0
            for di, dj in (
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ):
                x = i + di
                y = j + dj
                n += 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == "#"
            if (i, j) in (
                (0, 0),
                (0, len(grid[0]) - 1),
                (len(grid) - 1, 0),
                (len(grid) - 1, len(grid[0]) - 1),
            ):
                new_row.append("#")
            elif grid[i][j] == "#":
                if n in [2, 3]:
                    new_row.append("#")
                else:
                    new_row.append(".")
            else:
                if n == 3:
                    new_row.append("#")
                else:
                    new_row.append(".")
        new_grid.append(new_row)
    grid = new_grid

total = 0
for row in grid:
    for i in row:
        total += i == "#"

print("Part 2:", total)
