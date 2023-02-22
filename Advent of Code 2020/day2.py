old_policy = 0
new_policy = 0

for line in open("inputs/day2.in"):
    a, b, password = line.split()
    l, h = a.split("-")
    l = int(l)
    h = int(h)
    c = b[0]
    if l <= password.count(c) <= h:
        old_policy += 1
    if (password[l - 1] + password[h - 1]).count(c) == 1:
        new_policy += 1

print("Part 1:", old_policy)
print("Part 2:", new_policy)
