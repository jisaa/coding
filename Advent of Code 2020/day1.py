nums = [int(s) for s in open("inputs/day1.in")]


def f(nums, t):
    for i in nums:
        if t - i in nums:
            return i
    return -1


# part 1
print("part 1")
i = f(nums, 2020)
print(i, 2020 - i, i * (2020 - i))

# part 2
print()
print("part 2")
for x in nums:
    y = f(nums, 2020 - x)
    if y != -1:
        print(x, y, 2020 - x - y, x * y * (2020 - x - y))
        break
