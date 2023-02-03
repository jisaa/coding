f = open("inputs/day12.in")

grid = [[ord(c) for c in line.strip()] for line in f]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == ord("S"):
            start_i = i
            start_j = j
            grid[i][j] = ord("a")
        if grid[i][j] == ord("E"):
            end_i = i
            end_j = j
            grid[i][j] = ord("z")

steps = []
for row in grid:
    steps.append([99999] * len(row))
steps[start_i][start_j] = 0
q = [(start_i, start_j)]
while q:
    a, b = q.pop(0)
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x, y = a + di, b + dj
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] - grid[a][b] < 2:
            if steps[a][b] + 1 < steps[x][y]:
                steps[x][y] = steps[a][b] + 1
                q.append((x, y))

print("Part 1:", steps[end_i][end_j])


steps = []
for row in grid:
    steps.append([99999] * len(row))
steps[end_i][end_j] = 0
q = [(end_i, end_j)]
starts = []
while q:
    a, b = q.pop(0)
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x, y = a + di, b + dj
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[a][b] - grid[x][y] < 2:
            if steps[a][b] + 1 < steps[x][y]:
                steps[x][y] = steps[a][b] + 1
                q.append((x, y))
                if grid[x][y] == ord("a"):
                    starts.append(steps[x][y])

print("Part 2:", min(starts))
