winds = open("inputs/day17.in").readline().strip()
# winds = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

shapes = [
    [
        [1, 1, 1, 1],
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1],
    ],
    [
        [1],
        [1],
        [1],
        [1],
    ],
    [
        [1, 1],
        [1, 1],
    ],
]
"""
The tall, vertical chamber is exactly seven units wide.
Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).
"""

chamber = []
for _ in range(5000):
    chamber.append([0] * 7)


def new_rock_coords(chamber, rock):
    y = len(chamber) - 1
    while any(chamber[y]):
        y -= 1
    return [2, y - 2 - len(rock)]


def can_fall(chamber, rock, coords):
    if coords[1] + len(rock) == len(chamber):
        return False

    for i in range(len(rock)):
        for j in range(len(rock[i])):
            if rock[i][j] == 1 == chamber[coords[1] + i + 1][coords[0] + j]:
                return False
    return True


# TODO: arreglar
def can_blow(chamber, rock, coords, dir):
    if dir == -1 and coords[0] == 0:
        return False
    if coords[0] + dir + len(rock[0]) > len(chamber[0]):
        return False
    for i in range(len(rock)):
        for j in range(len(rock[i])):
            if rock[i][j] == 1 == chamber[coords[1] + i][coords[0] + j + dir]:
                return False
    return True


def tower_height(chamber):
    return len([x for x in chamber if any(x)])


wind_i = 0
shape_i = 0
for _fallen_rocks in range(2022):
    # appear
    shape = shapes[shape_i]
    shape_i += 1
    shape_i %= len(shapes)
    coords = new_rock_coords(chamber, shape)
    # print()
    # print(coords)

    # first wind
    dir = [1, -1][winds[wind_i] == "<"]
    coords[0] += dir
    wind_i += 1
    wind_i %= len(winds)
    # print(coords)

    while can_fall(chamber, shape, coords):
        # fall
        coords[1] += 1
        # print(coords)
        # apply wind
        dir = [1, -1][winds[wind_i] == "<"]
        if can_blow(chamber, shape, coords, dir):
            # print('blew', winds[wind_i])
            coords[0] += dir
        wind_i += 1
        wind_i %= len(winds)
        # print(coords)

    # place in chamber
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                chamber[coords[1] + i][coords[0] + j] = 1

print("Part 1:", tower_height(chamber))
