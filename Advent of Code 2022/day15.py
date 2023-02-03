def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class Sensor:
    def __init__(self, x, y, beacon):
        self.x = x
        self.y = y
        self.beacon = beacon
        self.d = manhattan_distance((self.x, self.y), beacon)

    def in_range(self, point):
        return manhattan_distance((self.x, self.y), point) <= self.d

    def __repr__(self) -> str:
        return f"{self.x} {self.y} {self.beacon} {self.d}"

    def perimeter(self):
        pr = (self.x, self.y + self.d + 1)
        pl = (self.x, self.y - self.d - 1)
        points = [pr, pl]
        for i in range(1, self.d + 2):
            points.append((pr[0] + i, pr[1] - i))
            points.append((pr[0] - i, pr[1] - i))
            points.append((pl[0] + i, pl[1] + i))
            points.append((pl[0] - i, pl[1] + i))

        return points


f = open("inputs/day15.in")

sensors = []
beacons = set()

for line in f:
    words = line.split()
    sx = int(words[2][2:-1])
    sy = int(words[3][2:-1])
    bx = int(words[8][2:-1])
    by = int(words[9][2:])
    beacon = (bx, by)
    sensor = Sensor(sx, sy, beacon)
    sensors.append(sensor)
    beacons.add(beacon)

target_y = 2000000
min_x = min([s.x - s.d for s in sensors] + [b[0] for b in beacons])
max_x = max([s.x + s.d for s in sensors] + [b[0] for b in beacons])

# this is really slow
used = 0
for x in range(min_x, max_x + 1):
    p = (x, target_y)
    if p in beacons:
        continue
    for s in sensors:
        if s.in_range(p):
            used += 1
            break
print("Part 1:", used)

# this is also slow, but not as much as part 1
max_coord = 4000000 + 1
for i in range(len(sensors)):
    for j in range(i + 1, len(sensors)):
        a = sensors[i]
        b = sensors[j]
        if manhattan_distance((a.x, a.y), (b.x, b.y)) > a.d + b.d:
            for p in a.perimeter():
                if p[0] < 0 or p[1] < 0 or p[0] > max_coord or p[1] > max_coord:
                    continue
                if all(not s.in_range(p) for s in sensors):
                    print("Part 2:", p[0] * 4000000 + p[1])
                    exit()
