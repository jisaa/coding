def calculate(s):
    if "(" in s:
        i = s.rindex("(")
        j = s.index(")", i)
        return calculate(s[:i] + str(calculate(s[i + 1 : j])) + s[j + 1 :])
    try:
        return int(s)
    except:
        pass
    s = s.split()
    if s[-2] == "+":
        return calculate(" ".join(s[:-2])) + int(s[-1])
    return calculate(" ".join(s[:-2])) * int(s[-1])


def calculateWithPrecedence(s):
    if "(" in s:
        i = s.rindex("(")
        j = s.index(")", i)
        return calculateWithPrecedence(
            s[:i] + str(calculateWithPrecedence(s[i + 1 : j])) + s[j + 1 :]
        )
    try:
        return int(s)
    except:
        pass
    s = s.split()
    if "+" in s:
        i = s.index("+")
        t = " ".join(s[: i - 1])
        t += " "
        t += str(int(s[i - 1]) + int(s[i + 1]))
        t += " "
        t += " ".join(s[i + 2 :])
        return calculateWithPrecedence(t)
    return calculateWithPrecedence(" ".join(s[:-2])) * int(s[-1])


total = 0
total2 = 0
for line in open("inputs/day18.in"):
    total += calculate(line.strip())
    total2 += calculateWithPrecedence(line.strip())

print("Part 1:", total)
print("Part 2:", total2)
