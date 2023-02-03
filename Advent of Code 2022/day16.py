f = open("p16.in")
lines = open("p16.in").readlines()

# save flow rates, edges and stuff
n_valves = len(lines)
connections = []
flow_rates = []
names = [line.split()[1] for line in lines]
aa_index = names.index("AA")

for i, line in enumerate(lines):
    words = line.split()
    name = words[1]
    flow = int(words[4][5:-1])
    others = tuple(w[:2] for w in words[9:])

    flow_rates.append(flow)
    connections.append([names.index(other) for other in others])

# calculate distance matrix
distances = []
for i in range(n_valves):
    distance = [9999] * n_valves
    visited = {i}.union(set(connections[i]))
    q = [(c, 1) for c in connections[i]]
    while q:
        j, d = q.pop(0)
        distance[j] = d
        for k in connections[j]:
            if k not in visited:
                q.append((k, d + 1))
                visited.add(k)
    distances.append(distance)

opened = [0] * n_valves
for i in range(n_valves):
    if flow_rates[i] == 0:
        opened[i] = 1

# position, opened, released_pressure, remaining_time
pending = [(aa_index, (0,) * n_valves, 0, 30)]
best = 0
while pending:
    position, opened, released_pressure, remaining_time = pending.pop()
    if released_pressure > best:
        best = released_pressure
        print(best, opened, remaining_time, len(pending))
    if remaining_time == 0 or all(opened):
        continue
    if remaining_time < 0:
        print("barf!!")
        print(position, opened, released_pressure, remaining_time)
        exit()
    for other in range(n_valves):
        # move to any closed valve and open it, check from there
        if opened[other] or distances[position][other] + 1 >= remaining_time:
            continue
        n_released_pressure = released_pressure + flow_rates[other] * (
            remaining_time - distances[position][other] - 1
        )
        n_opened = opened[:other] + (1,) + opened[other + 1 :]
        pending.append(
            (
                other,
                n_opened,
                n_released_pressure,
                remaining_time - distances[position][other] - 1,
            )
        )

print("Part 1:", best)

exit()
# 1777 too low for part 1


# brute force all paths
# position, opened, released_pressure, elapsed_time
pending = [(aa_index, (0,) * n_valves, 0, 0)]
best = 0
while pending:
    position, opened, released_pressure, elapsed_time = pending.pop()
    if elapsed_time == 30:
        if released_pressure > best:
            best = released_pressure
            print(best, len(pending))
        continue
    if all(opened):
        released_pressure += (30 - elapsed_time) * sum(
            opened[i] * flow_rates[i] for i in range(n_valves)
        )
        if released_pressure > best:
            best = released_pressure
            print(best, len(pending))
        continue
    released_pressure += sum(opened[i] * flow_rates[i] for i in range(n_valves))
    if not opened[position]:
        n_opened = opened[:position] + (1,) + opened[position + 1 :]
        pending.append((position, n_opened, released_pressure, elapsed_time + 1))
    for j, connected in enumerate(edges[position]):
        if connected:
            pending.append((j, opened, released_pressure, elapsed_time + 1))

print("Part 1:", best)
