import re


rules = {"|": "|"}
reading_rules = True
messages = []

for line in open("inputs/day19.in"):
    line = line.strip()
    if not line:
        reading_rules = False
        continue
    if reading_rules:
        n, r = line.split(": ")
        if '"' in r:
            rules[n] = r[1]
        else:
            rules[n] = r
    else:
        messages.append(line)


def expand(n, rules):
    x = rules[n]
    if any(d in x for d in "1234567890"):
        t = "(" + ") (".join(expand(p, rules) for p in x.split()) + ")"
        rules[n] = t.replace("(|)", "|").replace("(a)", "a").replace("(b)", "b")
    return rules[n]


pattern = "^" + expand("0", rules).replace(" ", "") + "$"
# print(pattern)

total = 0
for m in messages:
    if re.match(pattern, m):
        total += 1
print("Part 1:", total)

rules = {"|": "|"}
reading_rules = True

for line in open("inputs/day19.in"):
    line = line.strip()
    if not line:
        reading_rules = False
        continue
    if reading_rules:
        n, r = line.split(": ")
        if '"' in r:
            rules[n] = r[1]
        else:
            rules[n] = r


def expand2(n, rules):
    x = rules[n]
    if any(d in x for d in "1234567890"):
        t = "(" + ") (".join(expand2(p, rules) for p in x.split()) + ")"
        if n == "8":
            t = "(" + expand2("42", rules) + ")+"
        if n == "11":
            a = "(" + expand2("42", rules) + ")"
            b = "(" + expand2("31", rules) + ")"
            t = f"({a}{b})|({a}{a}{b}{b})|({a}{a}{a}{b}{b}{b})|({a}{a}{a}{a}{b}{b}{b}{b})"
        rules[n] = t.replace("(|)", "|").replace("(a)", "a").replace("(b)", "b")
    return rules[n]


pattern2 = "^" + expand2("0", rules).replace(" ", "") + "$"
# print(pattern2)

total2 = 0
for m in messages:
    if re.match(pattern2, m):
        total2 += 1
print("Part 2:", total2)
