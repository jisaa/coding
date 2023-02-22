path = open("inputs/day3.in").readline().strip()


def f(path):
    total = 1
    x = y = 0
    seen = {(0, 0)}

    for c in path:
        if c == "v":
            y -= 1
        elif c == "^":
            y += 1
        elif c == "<":
            x -= 1
        elif c == ">":
            x += 1
        seen.add((x, y))
    return seen


print("Part 1:", len(f(path)))

santa = f(path[::2])
robot = f(path[1::2])

print("Part 2:", len(santa | robot))
