def f(s, d):
    try:
        return int(s)
    except:
        pass
    op = d[s]
    try:
        return int(op)
    except:
        pass
    if "OR" in op:
        # |
        a, o, b = op.split()
        t = f(a, d) | f(b, d)
    elif "AND" in op:
        # &
        a, o, b = op.split()
        t = f(a, d) & f(b, d)
    elif "NOT" in op:
        # ^ 65535
        o, a = op.split()
        t = f(a, d) ^ 65535
    elif "LSHIFT" in op:
        # <<
        a, o, b = op.split()
        t = f(a, d) << f(b, d)
    elif "RSHIFT" in op:
        # >>
        a, o, b = op.split()
        t = f(a, d) >> f(b, d)
    else:
        t = f(op, d)
    d[s] = t
    return t


D = {}
for line in open("inputs/day7.in"):
    b, a = line.strip().split(" -> ")
    D[a] = b

sa = f("a", D)
print("Part 1:", sa)

e = {}
for line in open("inputs/day7.in"):
    b, a = line.strip().split(" -> ")
    e[a] = b
e["b"] = sa

print("Part 2:", f("a", e))
