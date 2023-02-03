def next(s):
    letters = "abcdefghjkmnpqrstuvwxyz"
    s = list(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "z":
            s[i] = "a"
        else:
            s[i] = letters[letters.index(s[i]) + 1]
            break
    return "".join(s)


def valid(s):
    run = 0
    for i in range(len(s) - 2):
        if ord(s[i]) + 2 == ord(s[i + 1]) + 1 == ord(s[i + 2]):
            run = 1
            break
    if not run:
        return False
    repeats = set()
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats.add(s[i])
    return len(repeats) > 1


start = next("cqjxjnds")
while not valid(start):
    start = next(start)
print("Part 1:", start)

start = next(start)
while not valid(start):
    start = next(start)
print("Part 2:", start)
