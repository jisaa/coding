map = [l.strip() for l in open("inputs/day3.in")]

result = 1
for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    trees = 0
    x = y = 0
    while y < len(map):
        if map[y][x % len(map[0])] == "#":
            trees += 1
        x += r
        y += d
    print(r, d, trees)
    result *= trees
print("Part 2:", result)
