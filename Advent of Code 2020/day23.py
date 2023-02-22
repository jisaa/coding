cups = [3, 9, 4, 6, 1, 8, 5, 2, 7]
# cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]


def next(cups, i):
    while i + 3 >= len(cups):
        cups = cups[1:] + [cups[0]]
        i -= 1
    t = cups[i + 1 : i + 4]
    cups[i + 1 : i + 4] = []

    go_after = cups[i] - 1
    while go_after in t or go_after == 0:
        if go_after in t:
            go_after -= 1
        if go_after == 0:
            go_after = max(cups)

    j = cups.index(go_after)
    cups[j + 1 : j + 1] = t
    if j < i:
        i += 3
    i += 1
    i %= len(cups)
    return cups, i


i = 0
for _ in range(100):
    cups, i = next(cups, i)
    # print(cups, i)

while cups[0] != 1:
    cups = cups[1:] + [cups[0]]

print("Part 1:", "".join(str(c) for c in cups[1:]))

cups = [3, 9, 4, 6, 1, 8, 5, 2, 7] + list(range(10, 1000000 + 1))

# TODO: optimize, this takes forever
i = 0
for _ in range(10000000):
    if _ % 10000 == 0:
        print(_)
    cups, i = next(cups, i)

i = cups.index(1)
print("Part 2:", cups[i + 1] * cups[i + 2])
