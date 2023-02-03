def far_away(h, t):
    return abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1


def follow(h, t):
    if t[0] < h[0] and t[1] < h[1]:
        t[0] += 1
        t[1] += 1
    elif t[0] > h[0] and t[1] < h[1]:
        t[0] -= 1
        t[1] += 1
    elif t[0] < h[0] and t[1] > h[1]:
        t[0] += 1
        t[1] -= 1
    elif t[0] > h[0] and t[1] > h[1]:
        t[0] -= 1
        t[1] -= 1
    elif t[0] < h[0]:
        t[0] += 1
    elif t[0] > h[0]:
        t[0] -= 1
    elif t[1] < h[1]:
        t[1] += 1
    elif t[1] > h[1]:
        t[1] -= 1


f = open("inputs/day9.in")
h = [0, 0]
t = [0, 0]
visited = {(0, 0)}
for line in f:
    direction, steps = line.split()
    steps = int(steps)
    for _ in range(steps):
        if direction == "R":
            h[0] += 1
        elif direction == "L":
            h[0] -= 1
        elif direction == "U":
            h[1] += 1
        else:  # direction == 'D':
            h[1] -= 1
        if far_away(h, t):
            follow(h, t)
        visited.add(tuple(t))

print("Part 1:", len(visited))

f = open("inputs/day9.in")
rope = []
for _ in range(10):
    rope.append([0, 0])
h = rope[0]
visited = {(0, 0)}
for line in f:
    direction, steps = line.split()
    steps = int(steps)
    for _ in range(steps):
        if direction == "R":
            h[0] += 1
        elif direction == "L":
            h[0] -= 1
        elif direction == "U":
            h[1] += 1
        else:  # direction == 'D':
            h[1] -= 1
        for i in range(1, 10):
            # b follows a
            a = rope[i - 1]
            b = rope[i]
            if far_away(a, b):
                follow(a, b)
        visited.add(tuple(rope[-1]))

print("Part 2:", len(visited))
