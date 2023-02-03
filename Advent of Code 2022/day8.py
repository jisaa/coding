f = open("inputs/day8.in")

trees = [[int(c) for c in line.strip()] for line in f]

total = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        visible = False
        if all(t < trees[i][j] for t in trees[i][:j]):
            visible = True
        if all(t < trees[i][j] for t in trees[i][j + 1 :]):
            visible = True
        if all(t < trees[i][j] for t in [trees[x][j] for x in range(i)]):
            visible = True
        if all(
            t < trees[i][j] for t in [trees[x][j] for x in range(i + 1, len(trees))]
        ):
            visible = True

        if visible:
            total += 1

print("Part 1:", total)

best_score = 0
for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1):
        left = right = up = down = 0
        # left
        for t in trees[i][:j][::-1]:
            left += 1
            if t >= trees[i][j]:
                break
        # right
        for t in trees[i][j + 1 :]:
            right += 1
            if t >= trees[i][j]:
                break
        # up
        for t in [trees[x][j] for x in range(i)][::-1]:
            up += 1
            if t >= trees[i][j]:
                break
        # down
        for t in [trees[x][j] for x in range(i + 1, len(trees))]:
            down += 1
            if t >= trees[i][j]:
                break

        score = left * right * up * down
        if score > best_score:
            best_score = score
        # print(i, j, trees[i][j], up, down, left, right, score)

print("Part 2:", best_score)
