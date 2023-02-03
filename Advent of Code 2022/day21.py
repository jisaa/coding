class Monkey:
    def __init__(self, name, rest):
        self.name = name
        self.waiting_for = []
        words = rest.split(" ")
        if len(words) == 1:
            self.done = True
            self.value = int(words[0])
        else:
            self.done = False
            self.waiting_for = [words[0], words[2]]
            self.operation = words[1]
            # if self.operation == "/":
            #    self.operation = "//"

    def __repr__(self) -> str:
        return f"{self.name} {self.done} {self.waiting_for}"


monkeys = {}
for line in open("inputs/day21.in").readlines():
    name, rest = line.strip().split(": ")
    monkeys[name] = Monkey(name, rest)


while not monkeys["root"].done:
    for name in monkeys:
        m = monkeys[name]
        if (
            not m.done
            and monkeys[m.waiting_for[0]].done
            and monkeys[m.waiting_for[1]].done
        ):
            m.done = True
            a = monkeys[m.waiting_for[0]].value
            b = monkeys[m.waiting_for[1]].value
            if m.operation == "+":
                m.value = a + b
            elif m.operation == "-":
                m.value = a - b
            elif m.operation == "*":
                m.value = a * b
            else:  # if m.operation == '/':
                m.value = a // b
print("Part 1:", monkeys["root"].value)


monkeys = {}
for line in open("inputs/day21.in").readlines():
    name, rest = line.strip().split(": ")
    monkeys[name] = Monkey(name, rest)
monkeys["humn"].value = "x"
monkeys["root"].operation = "="


def build_expression(monkey_name, monkeys):
    m = monkeys[monkey_name]
    if m.done:
        return str(m.value)
    t = f"({build_expression(m.waiting_for[0], monkeys)}) {m.operation} ({build_expression(m.waiting_for[1], monkeys)})"
    try:
        return str(eval(t))
    except:
        return t


equation = build_expression("root", monkeys).replace(".0", "")
print(equation)

print(
    "Part 2:",
    "go input that equation into https://www.mathpapa.com/equation-solver/ :P",
)
