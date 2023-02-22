def isNice1(s):
    if any(n in s for n in "ab cd pq xy".split()):
        return False
    vowels = 0
    repeated = 0
    for i in range(len(s)):
        if s[i] in "aeiou":
            vowels += 1
        if i and s[i] == s[i - 1]:
            repeated = 1

    return repeated and vowels > 2


def isNice2(s):
    first = 0
    second = 0
    for i in range(1, len(s)):
        if s[i - 1 : i + 1] in s[i + 1 :]:
            first = 1
        if i > 1 and s[i] == s[i - 2]:
            second = 1

    return first and second


total1 = 0
total2 = 0
for s in open("inputs/day5.in"):
    if isNice1(s.strip()):
        total1 += 1
    if isNice2(s.strip()):
        total2 += 1

print("Part 1:", total1)
print("Part 2:", total2)
