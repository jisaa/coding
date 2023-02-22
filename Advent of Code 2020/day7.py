m = {}
q = []
seen = []
for line in open("inputs/day7.in"):
    a, b = line.strip()[:-1].split(" bags contain")
    if "shiny gold" in b:
        q += (a,)
        seen += (a,)
    t = []
    for i in b.split(","):
        try:
            t.append((int(i.split()[0]), " ".join(i.split()[1:-1])))
        except:
            pass
    m[a] = t

while q:
    a = q.pop()
    for x in m:
        if x not in seen and a in (t[1] for t in m[x]):
            seen.append(x)
            q.append(x)

print("Part 1:", len(seen))


def f(x):
    r = 0
    for num, name in m[x]:
        r += num + num * f(name)
    return r


print("Part 2:", f("shiny gold"))
