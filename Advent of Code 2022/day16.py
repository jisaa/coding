lines = open("inputs/day16.in").readlines()

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


def path_time(path, distances):
    time = 0
    for i in range(1, len(path)):
        time += distances[path[i - 1]][path[i]] + 1
    return time


def is_valid_path(path, distances, final_time=30):
    return len(set(path)) == len(path) and path_time(path, distances) <= final_time


def released_pressure(path, flow_rates, distances, final_time=30):
    total = 0
    time = 0
    for i in range(1, len(path)):
        time += distances[path[i - 1]][path[i]] + 1
        total += (final_time - time) * flow_rates[path[i]]
    return total


def extend_path(prefix, n, flow_rates, distances, final_time=30, skip=[]):
    extended = []
    for i in range(n):
        if (
            i not in prefix
            and i not in skip
            and flow_rates[i] > 0
            and is_valid_path(prefix + [i], distances, final_time)
        ):
            extended.append(prefix + [i])
    return extended


def generate_final_paths(start, n_valves, distances, final_time=30, skip=[]):
    paths = [[start]]
    final_paths = []
    new_paths = True
    while new_paths:
        new_paths = False
        next_paths = []
        for path in paths:
            ep = extend_path(path, n_valves, flow_rates, distances, final_time, skip)
            if len(ep) > 0:
                next_paths.extend(ep)
                new_paths = True
            else:
                final_paths.append(path)
        paths = next_paths
    return final_paths


best = 0
for path in generate_final_paths(aa_index, n_valves, distances):
    rp = released_pressure(path, flow_rates, distances)
    if rp > best:
        best = rp
print("Part 1:", best)

# 10 minutes
best = 0
all_paths = generate_final_paths(aa_index, n_valves, distances, 26)
all_paths = tuple(tuple(p) for p in all_paths)
for i, my_path in enumerate(all_paths):
    for elephant_path in all_paths[i + 1 :]:
        if set(my_path).intersection(set(elephant_path)) == set([aa_index]):
            rp1 = released_pressure(my_path, flow_rates, distances, 26)
            rp2 = released_pressure(elephant_path, flow_rates, distances, 26)
            rp = rp1 + rp2
            if rp > best:
                best = rp
print("Part 2:", best)
