from functools import cmp_to_key


def in_order(a, b):
    if type(a) != type(b):
        # one int and one list
        if type(a) == int:
            a = [a]
        else:
            b = [b]
        return in_order(a, b)
    if type(a) == int:
        # two ints
        return a - b
    else:
        # two lists
        l = min(len(a), len(b))
        for i in range(l):
            t = in_order(a[i], b[i])
            if t == 0:
                continue
            return t
        return len(a) - len(b)


packets = []
packets.append([[2]])
packets.append([[6]])
i = 0
pair_index = 1
total = 0
lines = open("inputs/day13.in").readlines()
while i < len(lines):
    a = eval(lines[i])
    b = eval(lines[i + 1])
    i += 3
    if in_order(a, b) < 0:
        total += pair_index
    pair_index += 1
    packets.append(a)
    packets.append(b)
print("Part 1:", total)

packets.sort(key=cmp_to_key(in_order))
a = packets.index([[2]]) + 1
b = packets.index([[6]]) + 1
print("Part 2:", a * b)
