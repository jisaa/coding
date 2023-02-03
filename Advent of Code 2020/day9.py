numbers = list(map(int, open("inputs/day9.in")))


def valid(nums, x):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == x:
                return True
    return False


for i in range(25, len(numbers)):
    if not valid(numbers[i - 25 : i], numbers[i]):
        print("Part 1:", numbers[i])
        x = 0
        cur = numbers[0]
        y = 1
        while 1:
            if cur == numbers[i]:
                print("Part 2:", min(numbers[x:y]) + max(numbers[x:y]))
                break
            if cur > numbers[i]:
                cur -= numbers[x]
                x += 1
            else:
                cur += numbers[y]
                y += 1
        break
