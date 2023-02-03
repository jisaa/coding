"""
Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.
"""

deers = [
    [22, 8, 165],
    [8, 17, 114],
    [18, 6, 103],
    [25, 6, 145],
    [11, 12, 125],
    [21, 6, 121],
    [18, 3, 50],
    [20, 4, 75],
    [7, 20, 119],
]


def f(deer, end):
    speed, time, rest = deer
    q = 0  # 0:flying, 1:resting
    n = 0
    d = 0
    for t in range(end):
        if q == 0:
            d += speed
            n += 1
            if n == time:
                q = 1
                n = 0
        else:
            n += 1
            if n == rest:
                n = 0
                q = 0
    return d


print("Part 1:", max(f(deer, 2503) for deer in deers))

deers = [
    [22, 8, 165, 0, 0, 0, 0],
    [8, 17, 114, 0, 0, 0, 0],
    [18, 6, 103, 0, 0, 0, 0],
    [25, 6, 145, 0, 0, 0, 0],
    [11, 12, 125, 0, 0, 0, 0],
    [21, 6, 121, 0, 0, 0, 0],
    [18, 3, 50, 0, 0, 0, 0],
    [20, 4, 75, 0, 0, 0, 0],
    [7, 20, 119, 0, 0, 0, 0],
]

for t in range(2503):
    # advance one second
    for deer in deers:
        #        0      1     2     3  4  5  6
        # deer = speed, time, rest, q, n, d, points
        if deer[3] == 0:
            deer[5] += deer[0]
            deer[4] += 1
            if deer[4] == deer[1]:
                deer[3] = 1
                deer[4] = 0
        else:
            deer[4] += 1
            if deer[4] == deer[2]:
                deer[4] = 0
                deer[3] = 0
    # score a point to the leader
    best = 0
    for i in range(len(deers)):
        if deers[i][5] > deers[best][5]:
            best = i
    deers[best][6] += 1

winner = 0
for i in range(len(deers)):
    if deers[i][6] > deers[winner][6]:
        winner = i

print("Part 2:", deers[winner][6])
