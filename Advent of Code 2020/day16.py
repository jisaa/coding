rules = []
state = "rules"
others = []

for line in open("inputs/day16.in"):
    line = line.strip()
    if not line:
        continue
    if "your ticket" in line:
        state = "mine"
        continue
    if "nearby tickets" in line:
        state = "others"
        continue

    if state == "rules":
        rules.append(line)
    elif state == "mine":
        my_ticket = list(map(int, line.split(",")))
    else:
        others.append(list(map(int, line.split(","))))

rules_expanded = {}
valid = set()
for rule in rules:
    name, ranges = rule.split(": ")
    rules_expanded[name] = set()
    for r in ranges.split(" or "):
        a, b = map(int, r.split("-"))
        for i in range(a, b + 1):
            valid.add(i)
            rules_expanded[name].add(i)

valid_tickets = [my_ticket]
error_rate = 0
for ticket in others:
    is_valid = True
    for value in ticket:
        if value not in valid:
            error_rate += value
            is_valid = False
    if is_valid:
        valid_tickets.append(ticket)

print("Part 1:", error_rate)

n = len(rules_expanded)
names = sorted(rules_expanded.keys())
order = [-1] * n
possible = []

for name in names:
    t = []
    for i in range(n):
        if all(ticket[i] in rules_expanded[name] for ticket in valid_tickets):
            t.append(i)
    possible.append(t)

while any(len(p) > 1 for p in possible):
    for i in range(n):
        if len(possible[i]) > 1:
            continue
        t = possible[i][0]
        for j in range(n):
            if len(possible[j]) == 1:
                continue
            if t in possible[j]:
                possible[j].remove(t)

mult = 1
for i in range(n):
    if "departure" in names[i]:
        mult *= my_ticket[possible[i][0]]

print("Part 2:", mult)
