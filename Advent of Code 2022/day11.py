class Monkey:
    def __init__(self, lines):
        self.items = [int(i) for i in lines[0].strip().split(": ")[1].split(", ")]
        self.op = lines[1].strip().split(" = ")[1]
        self.test = int(lines[2].split()[-1])
        self.test_true = int(lines[3].split()[-1])
        self.test_false = int(lines[4].split()[-1])
        self.inspected = 0

    def __repr__(self) -> str:
        return f"{self.items} {self.op} {self.test} {self.test_true} {self.test_false}"


f = open("inputs/day11.in")
lines = f.readlines()
i = 0
monkeys = []
while i < len(lines):
    m = Monkey(lines[i + 1 : i + 6])
    monkeys.append(m)
    i += 7

rounds = 20
for _ in range(rounds):
    for i in range(len(monkeys)):
        while monkeys[i].items:
            monkeys[i].inspected += 1
            old = monkeys[i].items.pop(0)
            new = eval(monkeys[i].op) // 3
            if new % monkeys[i].test == 0:
                monkeys[monkeys[i].test_true].items.append(new)
            else:
                monkeys[monkeys[i].test_false].items.append(new)

values = [m.inspected for m in monkeys]
values.sort()
print("Part 1:", values[-1] * values[-2])

f = open("inputs/day11.in")
lines = f.readlines()
i = 0
divisor = 1
monkeys = []
while i < len(lines):
    m = Monkey(lines[i + 1 : i + 6])
    monkeys.append(m)
    divisor *= m.test
    i += 7

rounds = 10000
for _ in range(rounds):
    for i in range(len(monkeys)):
        while monkeys[i].items:
            monkeys[i].inspected += 1
            old = monkeys[i].items.pop(0)
            new = eval(monkeys[i].op) % divisor
            if new % monkeys[i].test == 0:
                monkeys[monkeys[i].test_true].items.append(new)
            else:
                monkeys[monkeys[i].test_false].items.append(new)

values = [m.inspected for m in monkeys]
values.sort()
print("Part 2:", values[-1] * values[-2])
