import json

x = json.load(open("inputs/day12.in"))


def partial(x, withoutRed=False):
    if type(x) == int:
        return x
    if type(x) == str:
        return 0
    if type(x) == list:
        return sum(partial(i, withoutRed) for i in x)
    if withoutRed and ("red" in x.values()):
        return 0
    return sum(partial(x[i], withoutRed) for i in x)


print("Part 1:", partial(x))
print("Part 2:", partial(x, True))
