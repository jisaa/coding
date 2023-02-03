start = "3113322113"


def n(s):
    next = ""
    cur = ""
    n = 0
    for c in s:
        if c == cur:
            n += 1
        else:
            if n:
                next += str(n) + cur
            cur = c
            n = 1

    return next + str(n) + cur


for _ in range(40):
    start = n(start)
print("Part 1:", len(start))

for _ in range(10):
    start = n(start)
print("Part 2:", len(start))
