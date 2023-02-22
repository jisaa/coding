instructions = []
for line in open("inputs/day8.in"):
    op, x = line.split()
    instructions += ([op, int(x)],)


def run():
    acc = 0
    seen = []
    curr = 0
    while curr < len(instructions):
        if curr in seen:
            return 0, acc
        seen.append(curr)
        op, x = instructions[curr]
        if op == "nop":
            curr += 1
        elif op == "acc":
            acc += x
            curr += 1
        else:
            curr += x
    return 1, acc


print("Part 1:", run()[1])

done = 0
for i in range(len(instructions)):
    for a, b in [["nop", "jmp"], ["jmp", "nop"]]:
        if instructions[i][0] == a:
            instructions[i][0] = b
            done, acc = run()
            if done:
                print("Part 2:", acc)
                break
            instructions[i][0] = a
    if done:
        break
