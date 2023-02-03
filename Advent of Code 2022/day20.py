numbers = list(map(int, open("inputs/day20.in").readlines()))
# numbers = [1, 2, -3, 3, -2, 0, 4]


def mix(numbers):
    # convert to [original_pos, number, in_original_position]
    if type(numbers[0]) == int:
        numbers = [[i, n, True] for i, n in enumerate(numbers)]
    else:
        for n in numbers:
            n[2] = True

    while any(t[2] for t in numbers):
        for i, t in enumerate(numbers):
            if t[2]:
                lowest = i
                break
        for i, t in enumerate(numbers):
            if t[2] and t[0] < numbers[lowest][0]:
                lowest = i
        t = numbers[lowest]
        t[2] = False
        numbers = numbers[:lowest] + numbers[lowest + 1 :]
        new_i = (lowest + t[1]) % len(numbers)
        if new_i == 0:
            new_i = len(numbers)
        numbers[new_i:new_i] = [t]

    return numbers


def get_coords(mixed):
    mixed = [t[1] for t in mixed]
    zero_i = mixed.index(0)
    total = 0
    for x in [1000, 2000, 3000]:
        total += mixed[(zero_i + x) % len(mixed)]
    return total


mixed = mix(numbers)
print("Part 1:", get_coords(mixed))

decryption_key = 811589153
numbers = [n * decryption_key for n in numbers]
for _mixing_rounds in range(10):
    numbers = mix(numbers)
print("Part 2:", get_coords(numbers))
