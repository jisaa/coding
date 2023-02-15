instructions = [line.strip() for line in open("inputs/day23.in").readlines()]


def execute(a, b):
    i = 0
    while 0 <= i < len(instructions):
        op = instructions[i][:3]
        if op == "hlf":
            if instructions[i][-1] == "a":
                a //= 2
            else:
                b //= 2
            i += 1
        elif op == "tpl":
            if instructions[i][-1] == "a":
                a *= 3
            else:
                b *= 3
            i += 1
        elif op == "inc":
            if instructions[i][-1] == "a":
                a += 1
            else:
                b += 1
            i += 1
        elif op == "jmp":
            offset = int(instructions[i][4:])
            i += offset
        elif op == "jie":
            offset = int(instructions[i][7:])
            if instructions[i][4] == "a" and a % 2 == 0:
                i += offset
            elif instructions[i][4] == "b" and b % 2 == 0:
                i += offset
            else:
                i += 1
        elif op == "jio":
            offset = int(instructions[i][7:])
            if instructions[i][4] == "a" and a == 1:
                i += offset
            elif instructions[i][4] == "b" and b == 1:
                i += offset
            else:
                i += 1
    return b


print("Part 1:", execute(0, 0))
print("Part 2:", execute(1, 0))
