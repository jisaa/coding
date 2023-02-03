f = open("inputs/day14.in")

rock = set()
max_y = 0
for line in f:
    points = line.strip().split(" -> ")
    prev = None
    for point in points:
        x, y = point.split(",")
        x = int(x)
        y = int(y)
        max_y = max(max_y, y)
        if prev is not None:
            a, b = prev
            while x < a:
                rock.add((a, b))
                a -= 1
            while x > a:
                rock.add((a, b))
                a += 1
            while y < b:
                rock.add((a, b))
                b -= 1
                max_y = max(max_y, b)
            while y > b:
                rock.add((a, b))
                b += 1
            rock.add((a, b))
        prev = (x, y)

sand = set()
while 1:
    x = 500
    y = 0
    while y < max_y:
        if (x, y + 1) in rock or (x, y + 1) in sand:
            if (x - 1, y + 1) in rock or (x - 1, y + 1) in sand:
                if (x + 1, y + 1) in rock or (x + 1, y + 1) in sand:
                    sand.add((x, y))
                    break
                else:
                    y += 1
                    x += 1
                    continue
            else:
                y += 1
                x -= 1
                continue
        else:
            y += 1
            continue
    else:
        break
print("Part 1:", len(sand))

min_x = min(p[0] for p in rock)
max_x = max(p[0] for p in rock)

for x in range(min_x - 1000, max_x + 1000):
    rock.add((x, max_y + 2))

sand = set()
while 1:
    x = 500
    y = 0
    while (500, 0) not in sand:
        if (x, y + 1) in rock or (x, y + 1) in sand:
            if (x - 1, y + 1) in rock or (x - 1, y + 1) in sand:
                if (x + 1, y + 1) in rock or (x + 1, y + 1) in sand:
                    sand.add((x, y))
                    break
                else:
                    y += 1
                    x += 1
                    continue
            else:
                y += 1
                x -= 1
                continue
        else:
            y += 1
            continue
    else:
        break
print("Part 2:", len(sand))
