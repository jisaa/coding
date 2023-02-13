containers = [int(line) for line in open("inputs/day17.in").readlines()]
liters = 150

ways = {}

used = [0] * len(containers)
used[0] = 1

# brute force all combinations
while any(used):
    capacity = sum(c * u for c, u in zip(containers, used))
    if capacity == liters:
        n = sum(used)
        ways[n] = ways.get(n, 0) + 1
    for i in range(len(used)):
        if used[i]:
            used[i] = 0
        else:
            used[i] = 1
            break

print("Part 1:", sum(ways.values()))
print("Part 2:", ways[min(ways.keys())])
