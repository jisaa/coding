def snafu_to_decimal(s):
    base = 1
    result = 0
    for c in s[::-1]:
        if c == "=":
            result += -2 * base
        if c == "-":
            result += -base
        if c == "1":
            result += base
        if c == "2":
            result += 2 * base
        base *= 5
    return result


def decimal_to_snafu(x):
    if x == 0:
        return "0"
    snafu = ""
    while x:
        snafu = "=-012"[(x + 2) % 5] + snafu
        x = (x + 2) // 5
    return snafu


total = 0
for line in open("inputs/day25.in"):
    line = line.strip()
    total += snafu_to_decimal(line)

print("Part 1:", decimal_to_snafu(total))
