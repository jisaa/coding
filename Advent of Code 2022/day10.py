f = open("inputs/day10.in")

register = 1
total = 0
cycle = 0
next_check = 20
crt = []
row = ""
pixel = 0
for line in f:
    if "noop" in line:
        cycle += 1
        if cycle == next_check:
            total += cycle * register
            next_check += 40
        if abs(register - pixel) < 2:
            row += "#"
        else:
            row += "."
        if len(row) == 40:
            crt.append(row)
            row = ""
        pixel += 1
        pixel %= 40
    else:
        _, value = line.split()
        value = int(value)
        cycle += 1
        if cycle == next_check:
            total += cycle * register
            next_check += 40
        if abs(register - pixel) < 2:
            row += "#"
        else:
            row += "."
        if len(row) == 40:
            crt.append(row)
            row = ""
        pixel += 1
        pixel %= 40
        cycle += 1
        if cycle == next_check:
            total += cycle * register
            next_check += 40
        if abs(register - pixel) < 2:
            row += "#"
        else:
            row += "."
        if len(row) == 40:
            crt.append(row)
            row = ""
        pixel += 1
        pixel %= 40
        register += value
    # print(cycle, register)

print("Part 1:", total)

print("Part 2:")
for row in crt:
    print(row)
