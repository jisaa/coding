f = open("inputs/day12.in")

edges = {}
for line in f:
    a, b = line.strip().split("-")
    if b != "start":
        edges[a] = edges.get(a, []) + [b]
    if a != "start":
        edges[b] = edges.get(b, []) + [a]


def advance(path, edges, paths=set()):
    if path[-1] == "end":
        paths.add(",".join(path))
    else:
        for node in edges[path[-1]]:
            if node == node.upper() or node not in path:
                advance(path + [node], edges)
    return paths


# all small caves visited up to twice
def advance2(path, edges, paths=set()):
    if path[-1] == "end":
        paths.add(",".join(path))
    else:
        for node in edges[path[-1]]:
            if can_extend(path, node):  # node == node.upper() or path.count(node) < 2:
                advance2(path + [node], edges)
    return paths


def can_extend(path, node):
    if node == node.upper() or node not in path:
        return True
    small_ones = [node for node in path[1:] if node == node.lower()]
    return len(small_ones) == len(set(small_ones))


print("Part 1:", len(advance(["start"], edges)))
print("Part 2:", len(advance2(["start"], edges)))
