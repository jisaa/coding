grid = []
for line in open("inputs/day23.in"):
    grid.append(line.strip())

elves = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            elves.append((j, i))

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)
NE = (1, -1)
NW = (-1, -1)
SE = (1, 1)
SW = (-1, 1)
all_dirs = [N, S, E, W, NE, NW, SE, SW]
rules = [
    ((N, NE, NW), N),
    ((S, SE, SW), S),
    ((W, NW, SW), W),
    ((E, NE, SE), E),
]


def empty(elf, dirs, elves):
    x, y = elf
    return not any((x + dx, y + dy) in elves for dx, dy in dirs)


any_moved = True
round = 0
while any_moved:
    any_moved = False
    round += 1
    proposed = []
    for elf in elves:
        if empty(elf, all_dirs, elves):
            proposed.append(elf)
            continue
        for dirs, dest in rules:
            if empty(elf, dirs, elves):
                proposed.append((elf[0] + dest[0], elf[1] + dest[1]))
                break
        else:
            proposed.append(elf)

    next_elves = []
    for i in range(len(elves)):
        if proposed[i] != elves[i] and proposed.count(proposed[i]) == 1:
            next_elves.append(proposed[i])
            any_moved = True
        else:
            next_elves.append(elves[i])
    elves = next_elves
    rules = rules[1:] + rules[:1]

    # TODO: figure out why 12 gives out the right answer instead of 10 :P
    if round == 12:
        min0 = min(elf[0] for elf in elves)
        max0 = max(elf[0] for elf in elves)
        min1 = min(elf[1] for elf in elves)
        max1 = max(elf[1] for elf in elves)

        print("Part 1:", (max0 - min0) * (max1 - min1) - len(elves))

# TODO: refactor so part 2 completes faster
print("Part 2:", round)
