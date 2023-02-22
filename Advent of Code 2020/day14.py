d = {}


def f(value, mask):
    b = bin(value)[2:]
    b = list("0" * (len(mask) - len(b)) + b)
    for i in range(len(b)):
        if mask[i] != "X":
            b[i] = mask[i]
    return int("".join(b), 2)


for line in open("inputs/day14.in"):
    op, value = line.strip().split(" = ")
    if op == "mask":
        mask = value
    else:
        address = int(op[4:-1])
        value = int(value)
        d[address] = f(value, mask)

print("Part 1:", sum(d.values()))


d = {}


def m(value, mask):
    b = bin(value)[2:]
    b = list("0" * (len(mask) - len(b)) + b)
    for i in range(len(b)):
        if mask[i] != "0":
            b[i] = mask[i]
    return b


def get_addresses(b):
    if "X" not in b:
        return [int("".join(b), 2)]
    i = b.index("X")
    b[i] = "0"
    t = get_addresses(b)
    b[i] = "1"
    t += get_addresses(b)
    b[i] = "X"
    return t


for line in open("inputs/day14.in"):
    op, value = line.strip().split(" = ")
    if op == "mask":
        mask = value
    else:
        address = int(op[4:-1])
        value = int(value)
        for address in get_addresses(m(address, mask)):
            d[address] = value

print("Part 2:", sum(d.values()))
