f = open("inputs/day13.in")
current_time = int(f.readline())
buses = f.readline().split(",")
ids = [int(b) for b in buses if b != "x"]

t = 0
while not any((current_time + t) % b == 0 for b in ids):
    t += 1

for b in ids:
    if (current_time + t) % b == 0:
        print("Part 1:", b * t)

max_id = max(ids)
max_i = buses.index(str(max_id))


# custom made for the problem input
# print(ids)
# print([buses.index(str(i)) for i in ids])
# offsets = [ 0,   3,  13, 25, 30, 42,  44, 50, 67]
# print([i-13 for i in offsets])
ids = [13, 41, 467, 19, 17, 29, 353, 37, 23]
offsets = [-13, -10, 0, 12, 17, 29, 31, 37, 54]

ids = [41, 19, 353, 23]
offsets = [-10, 12, 31, 54]

step = 467 * 13 * 17 * 29 * 37

t = step
while 1:
    if all((t + buses.index(str(id)) - max_i) % id == 0 for id in ids):
        print("Part 2:", t - max_i)
        break
    t += step
