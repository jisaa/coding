def presents(house):
    t = 1 + house
    d = 2
    while d * d < house:
        if house % d == 0:
            t += d
            t += house // d
        d += 1
    if d * d == house:
        t += d
    return 10 * t


target = 29000000  # problem input

house = 1
while presents(house) < target:
    house += 1
print("Part 1:", house)


def presents2(house):
    t = 1 + house
    d = 2
    while d * d < house:
        if house % d == 0:
            if house // d <= 50:
                t += d
            if d <= 50:
                t += house // d
        d += 1
    if d * d == house:
        t += d
    return 11 * t


house = 1
while presents2(house) < target:
    house += 1
print("Part 2:", house)
