start = []
for line in open("inputs/day17.in"):
    start.append(list(line.strip()))

world = [start]

for _ in range(6):
    new_world = []
    for z in range(-1, len(world) + 1):
        level = []
        for i in range(-1, len(world[0]) + 1):
            row = []
            for j in range(-1, len(world[0][0]) + 1):
                near = 0
                for dz in [-1, 0, 1]:
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if dz == di == dj == 0:
                                continue
                            if (
                                0 <= z + dz < len(world)
                                and 0 <= i + di < len(world[0])
                                and 0 <= j + dj < len(world[0][0])
                            ):
                                near += world[z + dz][i + di][j + dj] == "#"
                active = 0
                if (
                    0 <= z < len(world)
                    and 0 <= i < len(world[0])
                    and 0 <= j < len(world[0][0])
                ):
                    active = world[z][i][j] == "#"
                # print(z, i, j, near, active)
                if active:
                    if near == 2 or near == 3:
                        row.append("#")
                    else:
                        row.append(".")
                else:
                    if near == 3:
                        row.append("#")
                    else:
                        row.append(".")
            level.append(row)
            # print(''.join(row))
        new_world.append(level)
    world = new_world

total = 0
for z in range(len(world)):
    for i in range(len(world[0])):
        for j in range(len(world[0][0])):
            total += world[z][i][j] == "#"

print("Part 1:", total)


start = []
for line in open("inputs/day17.in"):
    start.append(line.strip())

world = [[start]]

for _ in range(6):
    new_world = []
    for a in range(-1, len(world) + 1):
        x = []
        for b in range(-1, len(world[0]) + 1):
            y = []
            for c in range(-1, len(world[0][0]) + 1):
                z = []
                for d in range(-1, len(world[0][0][0]) + 1):
                    near = 0
                    for da in [-1, 0, 1]:
                        for db in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                for dd in [-1, 0, 1]:
                                    if da == db == dc == dd == 0:
                                        continue
                                    if (
                                        0 <= a + da < len(world)
                                        and 0 <= b + db < len(world[0])
                                        and 0 <= c + dc < len(world[0][0])
                                        and 0 <= d + dd < len(world[0][0][0])
                                    ):
                                        near += (
                                            world[a + da][b + db][c + dc][d + dd] == "#"
                                        )

                    active = 0
                    if (
                        0 <= a < len(world)
                        and 0 <= b < len(world[0])
                        and 0 <= c < len(world[0][0])
                        and 0 <= d < len(world[0][0][0])
                    ):
                        active = world[a][b][c][d] == "#"
                    if active:
                        if near == 2 or near == 3:
                            z.append("#")
                        else:
                            z.append(".")
                    else:
                        if near == 3:
                            z.append("#")
                        else:
                            z.append(".")
                y.append(z)
            x.append(y)
        new_world.append(x)
    world = new_world

total = 0
for a in world:
    for b in a:
        for c in b:
            for d in c:
                total += d == "#"

print("Part 2:", total)
