nums = [9, 19, 1, 6, 0, 5, 4]
d = {nums[i]: [i] for i in range(len(nums))}

n = len(nums)
prev = nums[-1]
while n < 2020:
    if len(d[prev]) == 1:
        d[0].append(n)
        prev = 0
    else:
        k = d[prev][-1] - d[prev][-2]
        if k not in d:
            d[k] = []
        d[k].append(n)
        prev = k
    n += 1
print("Part 1:", prev)


while n < 30000000:
    if len(d[prev]) == 1:
        d[0].append(n)
        prev = 0
    else:
        k = d[prev][-1] - d[prev][-2]
        if k not in d:
            d[k] = [n]
        else:
            d[k] = [d[k][-1], n]
        prev = k
    n += 1
print("Part 2:", prev)
