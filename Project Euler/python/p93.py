"""
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations
(+, -, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) - 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum,
and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers,
1 to n, can be obtained, giving your answer as a string: abcd.
"""

base_expressions = [
    "n. op n. op n. op n.",
    "(n. op n.) op n. op n.",
    "(n. op n. op n.) op n.",
    "(n. op n.) op (n. op n.)",
    "n. op (n. op n.) op n.",
    "n. op (n. op n. op n.)",
    "n. op n. op (n. op n.)",
    "(n. op (n. op n.)) op n.",
    "n. op ((n. op n.) op n.)",
    "((n. op n.) op n.) op n.",
    "n. op (n. op (n. op n.))",
]
operators = ["+", "-", "*", "/"]
expressions = []
for exp in base_expressions:
    exp = exp.split("op")
    for opa in operators:
        for opb in operators:
            for opc in operators:
                t = exp[0] + opa + exp[1] + opb + exp[2] + opc + exp[3]
                expressions.append(t)

best = 0
result = []
n = 0
for a in range(10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            for d in range(c + 1, 10):
                values = set()
                for exp in expressions:
                    exp = exp.split("n")
                    possibles = []
                    possibles.append(
                        exp[0]
                        + str(a)
                        + exp[1]
                        + str(b)
                        + exp[2]
                        + str(c)
                        + exp[3]
                        + str(d)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(a)
                        + exp[1]
                        + str(b)
                        + exp[2]
                        + str(d)
                        + exp[3]
                        + str(c)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(a)
                        + exp[1]
                        + str(d)
                        + exp[2]
                        + str(c)
                        + exp[3]
                        + str(b)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(a)
                        + exp[1]
                        + str(d)
                        + exp[2]
                        + str(b)
                        + exp[3]
                        + str(c)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(a)
                        + exp[1]
                        + str(c)
                        + exp[2]
                        + str(b)
                        + exp[3]
                        + str(d)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(a)
                        + exp[1]
                        + str(c)
                        + exp[2]
                        + str(d)
                        + exp[3]
                        + str(b)
                        + exp[4]
                    )

                    possibles.append(
                        exp[0]
                        + str(b)
                        + exp[1]
                        + str(a)
                        + exp[2]
                        + str(c)
                        + exp[3]
                        + str(d)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(b)
                        + exp[1]
                        + str(a)
                        + exp[2]
                        + str(d)
                        + exp[3]
                        + str(c)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(b)
                        + exp[1]
                        + str(c)
                        + exp[2]
                        + str(a)
                        + exp[3]
                        + str(d)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(b)
                        + exp[1]
                        + str(c)
                        + exp[2]
                        + str(d)
                        + exp[3]
                        + str(a)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(b)
                        + exp[1]
                        + str(d)
                        + exp[2]
                        + str(c)
                        + exp[3]
                        + str(a)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(b)
                        + exp[1]
                        + str(d)
                        + exp[2]
                        + str(a)
                        + exp[3]
                        + str(c)
                        + exp[4]
                    )

                    possibles.append(
                        exp[0]
                        + str(c)
                        + exp[1]
                        + str(a)
                        + exp[2]
                        + str(b)
                        + exp[3]
                        + str(d)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(c)
                        + exp[1]
                        + str(a)
                        + exp[2]
                        + str(d)
                        + exp[3]
                        + str(b)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(c)
                        + exp[1]
                        + str(b)
                        + exp[2]
                        + str(a)
                        + exp[3]
                        + str(d)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(c)
                        + exp[1]
                        + str(b)
                        + exp[2]
                        + str(d)
                        + exp[3]
                        + str(a)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(c)
                        + exp[1]
                        + str(d)
                        + exp[2]
                        + str(a)
                        + exp[3]
                        + str(b)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(c)
                        + exp[1]
                        + str(d)
                        + exp[2]
                        + str(b)
                        + exp[3]
                        + str(a)
                        + exp[4]
                    )

                    possibles.append(
                        exp[0]
                        + str(d)
                        + exp[1]
                        + str(a)
                        + exp[2]
                        + str(b)
                        + exp[3]
                        + str(c)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(d)
                        + exp[1]
                        + str(a)
                        + exp[2]
                        + str(c)
                        + exp[3]
                        + str(b)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(d)
                        + exp[1]
                        + str(b)
                        + exp[2]
                        + str(a)
                        + exp[3]
                        + str(c)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(d)
                        + exp[1]
                        + str(b)
                        + exp[2]
                        + str(c)
                        + exp[3]
                        + str(a)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(d)
                        + exp[1]
                        + str(c)
                        + exp[2]
                        + str(a)
                        + exp[3]
                        + str(b)
                        + exp[4]
                    )
                    possibles.append(
                        exp[0]
                        + str(d)
                        + exp[1]
                        + str(c)
                        + exp[2]
                        + str(b)
                        + exp[3]
                        + str(a)
                        + exp[4]
                    )

                    for p in possibles:
                        t = a + b + c + d
                        try:
                            t = eval(p)
                        except:
                            pass
                        values.add(t)

                values = [int(i) for i in sorted(values) if i == int(i) and i > 0]
                i = 1
                while i - 1 < len(values) and values[i - 1] == i:
                    i += 1
                if i > best:
                    best = i
                    result = a, b, c, d
                    print(best - 1, result)  # , values
