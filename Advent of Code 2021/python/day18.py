def add(n1, n2):
    return [n1, n2]


def can_explode(n, depth=0):
    if depth > 4:
        return True
    if type(n) is int:
        return False
    a, b = n
    return can_explode(a, depth + 1) or can_explode(b, depth + 1)


def explode(n):
    ns = list(str(n))
    depth = 0
    for i in range(len(ns)):
        if ns[i] == "[":
            depth += 1
        elif ns[i] == "]":
            depth -= 1
        elif depth == 5:
            a = ns[i]
            j = 1
            while ns[i + j] in "1234567890":
                a += ns[i + j]
                j += 1
            while ns[i + j] not in "1234567890":
                j += 1
            b = ns[i + j]
            j += 1
            while ns[i + j] in "1234567890":
                b += ns[i + j]
                j += 1
            # replace pair with 0 at position i-1
            ns = ns[: i - 1] + ["0"] + ns[i + j + 1 :]

            # add b to the right
            j = i
            while j < len(ns) and ns[j] not in "1234567890":
                j += 1
            if j < len(ns):
                right = ns[j]
                k = 1
                while ns[j + k] in "1234567890":
                    right += ns[j + k]
                    k += 1
                right = str(int(right) + int(b))
                ns[j : j + k] = right

            # add a to the left
            j = i - 2
            while j > 0 and ns[j] not in "1234567890":
                j -= 1
            if j > 0:
                left = ns[j]
                k = 1
                while ns[j - k] in "1234567890":
                    left = ns[j - k] + left
                    k += 1
                left = str(int(left) + int(a))
                ns[j - k + 1 : j + 1] = left

            return eval("".join(ns))


def can_split(n):
    for i in n:
        if type(i) is list:
            if can_split(i):
                return True
        else:
            if i > 9:
                return True
    return False


def split(n):
    if type(n) is int:
        return False
    a, b = n
    if type(a) is int:
        if a > 9:
            n[0] = [a // 2, (a + 1) // 2]
            return True
    else:
        if split(a):
            return True
    if type(b) is int and b > 9:
        n[1] = [b // 2, (b + 1) // 2]
        return True
    return split(b)


def reduce(n):
    # rint('...', n)
    if can_explode(n):
        n = explode(n)
        return reduce(n)
    if can_split(n):
        split(n)
        return reduce(n)
    return n


def magnitude(n):
    if type(n) is int:
        return n
    a, b = n
    return 3 * magnitude(a) + 2 * magnitude(b)


f = open("inputs/day18.in")
num = eval(f.readline().strip())
for line in f:
    b = eval(line.strip())
    # print('+', b)
    num = add(num, b)
    num = reduce(num)
    # print('=', num)
    # print()

print("Part 1:", magnitude(num))

f = open("inputs/day18.in")
nums = []
for line in f:
    nums.append(eval(line.strip()))

n = len(nums)
largest_magnitude = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a = nums[i]
        b = nums[j]
        c = reduce(add(a, b))
        m = magnitude(c)
        if m > largest_magnitude:
            largest_magnitude = m
        c = reduce(add(b, a))
        m = magnitude(c)
        if m > largest_magnitude:
            largest_magnitude = m

print("Part 2:", largest_magnitude)
