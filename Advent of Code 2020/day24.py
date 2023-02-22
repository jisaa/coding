black = set()

for line in open("inputs/day24.in"):
    line = line.strip()
    i = 0
    x = y = 0
    while i < len(line):
        dx = 2
        if line[i] == "n":
            y += 1
            dx = 1
            i += 1
        if line[i] == "s":
            y -= 1
            dx = 1
            i += 1

        if line[i] == "e":
            x += dx
        if line[i] == "w":
            x -= dx
        i += 1
    t = (x, y)
    if t not in black:
        black.add(t)
    else:
        black.remove(t)

print("Part 1:", len(black))


def neighbors(x, y):
    return (
        (x + 2, y),
        (x - 2, y),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    )


for _ in range(100):
    new_black = set()
    for x, y in black:
        bn = 0
        for n in neighbors(x, y):
            if n in black:
                bn += 1
            if n not in black:
                bnn = 0
                for nn in neighbors(n[0], n[1]):
                    if nn in black:
                        bnn += 1
                if bnn == 2:
                    new_black.add(n)
        if bn == 1 or bn == 2:
            new_black.add((x, y))
    black = new_black

print("Part 2:", len(black))
