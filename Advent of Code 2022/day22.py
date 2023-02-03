f = open("inputs/day22.in")

longest_line = 0
grid = []
reading_grid = True
for line in f:
    line = line[:-1]
    if reading_grid:
        if line:
            grid.append(line)
            longest_line = max(longest_line, len(line))
        else:
            reading_grid = False
    else:
        path = line

# normalize line lengths
for i in range(len(grid)):
    grid[i] = grid[i] + " " * (longest_line - len(grid[i]) + 1)

# parse path
steps = []
turns = []
cur = ""
for c in path:
    if c in "LR":
        steps.append(int(cur))
        cur = ""
        turns.append(c)
    else:
        cur += c
steps.append(int(cur))
turns.append("")

x = grid[0].index(".")
y = 0
facing = "right"

# coords = grid[y][x]
for step, turn in zip(steps, turns):
    # move
    dx, dy = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }[facing]
    for _ in range(step):
        a, b = x + dx, y + dy
        b %= len(grid)
        a %= len(grid[b])
        while grid[b][a] == " ":
            a, b = a + dx, b + dy
            b %= len(grid)
            a %= len(grid[b])
        if grid[b][a] == "#":
            break
        x, y = a, b

    # turn
    if turn == "R":
        if facing == "right":
            facing = "down"
        elif facing == "down":
            facing = "left"
        elif facing == "left":
            facing = "up"
        else:  # if facing == 'up':
            facing = "right"
    elif turn == "L":
        if facing == "right":
            facing = "up"
        elif facing == "down":
            facing = "right"
        elif facing == "left":
            facing = "down"
        else:  # if facing == 'up':
            facing = "left"

row = y + 1
col = x + 1
fac = {
    "right": 0,
    "down": 1,
    "left": 2,
    "up": 3,
}[facing]

print("Part 1:", 1000 * row + 4 * col + fac)

# 96278 too high
