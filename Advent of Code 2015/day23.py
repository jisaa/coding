instructions = [line.strip() for line in open("inputs/day23.in").readlines()]


def execute(a, b):
    i = 0
    registers = {"a": a, "b": b}
    while 0 <= i < len(instructions):
        op = instructions[i][:3]
        if op == "hlf":
            registers[instructions[i][4]] //= 2
            i += 1
        elif op == "tpl":
            registers[instructions[i][4]] *= 3
            i += 1
        elif op == "inc":
            registers[instructions[i][4]] += 1
            i += 1
        elif op == "jmp":
            offset = int(instructions[i][4:])
            i += offset
        elif op == "jie":
            offset = int(instructions[i][7:])
            if registers[instructions[i][4]] % 2 == 0:
                i += offset
            else:
                i += 1
        elif op == "jio":
            offset = int(instructions[i][7:])
            if registers[instructions[i][4]] == 1:
                i += offset
            else:
                i += 1
    return registers["b"]


print("Part 1:", execute(0, 0))
print("Part 2:", execute(1, 0))
