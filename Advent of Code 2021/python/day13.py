f = open("inputs/day13.in")

dots = []
for line in f:
    line = line.strip()
    if line:
        x, y = line.split(",")
        dots.append([int(x), int(y)])
    else:
        break

instructions = []
for line in f:
    instructions.append(line.strip()[11:])

for instruction in instructions:
    dir, n = instruction.split("=")
    fold = int(n)
    if dir == "y":
        for dot in dots:
            if dot[1] > fold:
                dot[1] = 2 * fold - dot[1]
    else:
        for dot in dots:
            if dot[0] > fold:
                dot[0] = 2 * fold - dot[0]
    break

sdots = [f"{d[0]},{d[1]}" for d in dots]
print("Part 1:", len(set(sdots)))

for instruction in instructions[1:]:
    dir, n = instruction.split("=")
    fold = int(n)
    if dir == "y":
        for dot in dots:
            if dot[1] > fold:
                dot[1] = 2 * fold - dot[1]
    else:
        for dot in dots:
            if dot[0] > fold:
                dot[0] = 2 * fold - dot[0]

max_x = max_y = 0
for x, y in dots:
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
print("Part 2:")
for y in range(max_y + 1):
    line = ""
    for x in range(max_x + 1):
        if [x, y] in dots:
            line += "#"
        else:
            line += " "
    print(line)
