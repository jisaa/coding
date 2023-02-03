f = open("inputs/day18.in")
cubes = []
for line in f.readlines():
    x, y, z = line.strip().split(",")
    cubes.append((int(x), int(y), int(z)))

"""# slow brute force
def share_a_side(a, b):
    if a[0] == b[0] and a[1] == b[1] and abs(a[2] - b[2]) == 1:
        return True
    if a[0] == b[0] and a[2] == b[2] and abs(a[1] - b[1]) == 1:
        return True
    if a[2] == b[2] and a[1] == b[1] and abs(a[0] - b[0]) == 1:
        return True
    return False


surface_area = 6 * len(cubes)
for i in range(len(cubes)):
    for j in range(i + 1, len(cubes)):
        if share_a_side(cubes[i], cubes[j]):
            surface_area -= 2
print("Part 1:", surface_area)
"""

cubes = set(cubes)
surface_area = 6 * len(cubes)
for x, y, z in cubes:
    for dx, dy, dz in (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ):
        a = x + dx
        b = y + dy
        c = z + dz
        if (a, b, c) in cubes:
            surface_area -= 1
print("Part 1:", surface_area)


min_x = min(c[0] for c in cubes)
max_x = max(c[0] for c in cubes)
min_y = min(c[1] for c in cubes)
max_y = max(c[1] for c in cubes)
min_z = min(c[2] for c in cubes)
max_z = max(c[2] for c in cubes)

outside = set()
q = [(min_x - 1, min_y - 1, min_z - 1)]
while q:
    x, y, z = q.pop()
    for dx, dy, dz in (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ):
        a = x + dx
        b = y + dy
        c = z + dz
        if (a, b, c) in cubes:
            continue
        if (
            a + 1 < min_x
            or a - 1 > max_x
            or b + 1 < min_y
            or b - 1 > max_y
            or c + 1 < min_z
            or c - 1 > max_z
        ):
            continue
        if (a, b, c) in outside:
            continue
        outside.add((a, b, c))
        q.append((a, b, c))

# print(outside)

# fill up all interior spaces with cubes
for x in range(min_x + 1, max_x):
    for y in range(min_y + 1, max_y):
        for z in range(min_z + 1, max_z):
            if (x, y, z) in cubes:
                continue
            different_x = [c for c in cubes if c[1] == y and c[2] == z]
            different_y = [c for c in cubes if c[0] == x and c[2] == z]
            different_z = [c for c in cubes if c[0] == x and c[1] == y]
            if (
                any(c[0] < x for c in different_x)
                and any(c[0] > x for c in different_x)
                and any(c[1] < y for c in different_y)
                and any(c[1] > y for c in different_y)
                and any(c[2] < z for c in different_z)
                and any(c[2] > z for c in different_z)
            ):
                # (x,y,z) is a cube that can see existing cubes in all 6 directions
                if (x, y, z) not in outside:
                    cubes.add((x, y, z))

# recalculate
surface_area = 6 * len(cubes)
for x, y, z in cubes:
    for dx, dy, dz in (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ):
        a = x + dx
        b = y + dy
        c = z + dz
        if (a, b, c) in cubes:
            surface_area -= 1
print("Part 2:", surface_area)
