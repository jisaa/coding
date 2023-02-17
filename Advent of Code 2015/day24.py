from itertools import combinations


def quantum_entanglement(values):
    q = 1
    for v in values:
        q *= v
    return q


def get_weight(weights, selected):
    return sum(w * s for (w, s) in zip(weights, selected))


def get_group(weights, parts, mem={3: [], 4: []}):
    used = mem[parts]
    while len(used) < len(weights):
        used.append(0)
    while 1:
        for i in range(len(used)):
            if used[i]:
                used[i] = 0
            else:
                used[i] = 1
                break
        if parts * get_weight(weights, used) == sum(weights):
            yield used
        if all(used):
            return


def get_next_group(weights, parts, selected):
    used = [0] * len(weights)
    while 1:
        for i in range(len(used)):
            if used[i]:
                used[i] = 0
            elif selected[i] == 0:
                used[i] = 1
                break
        if parts * get_weight(weights, used) == sum(weights):
            return used
        if all([a + b for a, b in zip(used, selected)]):
            raise


weights = [int(line) for line in open("inputs/day24.in")]

first_group = next(get_group(weights, 3))
second_group = get_next_group(weights, 3, first_group)
third_group = [1 if a + b == 0 else 0 for a, b in zip(first_group, second_group)]

smallest_group_size = len(weights)
smallest_qe = quantum_entanglement(weights)
for group in (first_group, second_group, third_group):
    q = quantum_entanglement([a for a, b in zip(weights, group) if b])
    if sum(group) < smallest_group_size:
        smallest_group_size = sum(group)
        smallest_group = group
        smallest_qe = q
    elif q < smallest_qe:
        smallest_qe = q

target = sum(weights) // 3
for other in combinations(weights, smallest_group_size):
    if sum(other) == target:
        q = quantum_entanglement(other)
        if q < smallest_qe:
            smallest_qe = q


print("Part 1:", smallest_qe)

for first_group in get_group(weights, 4):
    try:
        second_group = get_next_group(weights, 4, first_group)
        third_group = get_next_group(
            weights, 4, [a + b for a, b in zip(first_group, second_group)]
        )
        break
    except:
        continue

fourth_group = [
    1 if a + b + c == 0 else 0
    for a, b, c in zip(first_group, second_group, third_group)
]
smallest_group_size = len(weights)
smallest_qe = quantum_entanglement(weights)
for group in (first_group, second_group, third_group, fourth_group):
    q = quantum_entanglement([a for a, b in zip(weights, group) if b])
    if sum(group) < smallest_group_size:
        smallest_group_size = sum(group)
        smallest_group = group
        smallest_qe = q
    elif q < smallest_qe:
        smallest_qe = q

target = sum(weights) // 4
for other in combinations(weights, smallest_group_size):
    if sum(other) == target:
        q = quantum_entanglement(other)
        if q < smallest_qe:
            smallest_qe = q


print("Part 2:", smallest_qe)
