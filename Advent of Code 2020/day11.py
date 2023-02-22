board = [list(line.strip()) for line in open("inputs/day11.in")]

changes = 1
while changes:
    changes = 0
    t = []
    for _ in board:
        t.append(["."] * len(_))

    for i in range(len(board)):
        for j in range(len(board[0])):
            t[i][j] = board[i][j]
            if board[i][j] == ".":
                continue
            n = 0
            for di, dj in [
                [0, 1],
                [0, -1],
                [1, 0],
                [1, 1],
                [1, -1],
                [-1, 0],
                [-1, 1],
                [-1, -1],
            ]:
                ni = i + di
                nj = j + dj
                if (
                    0 <= ni < len(board)
                    and 0 <= nj < len(board[0])
                    and board[ni][nj] == "#"
                ):
                    n += 1
            if board[i][j] == "L":
                if n == 0:
                    t[i][j] = "#"
                    changes = 1
            elif board[i][j] == "#":
                if n > 3:
                    t[i][j] = "L"
                    changes = 1
    board = t

used = sum(sum(1 for i in r if i == "#") for r in board)
print("Part 1:", used)

board = [list(line.strip()) for line in open("inputs/day11.in")]

changes = 1
while changes:
    changes = 0
    t = []
    for _ in board:
        t.append(["."] * len(_))

    for i in range(len(board)):
        for j in range(len(board[0])):
            t[i][j] = board[i][j]
            if board[i][j] == ".":
                continue
            n = 0
            for di, dj in [
                [0, 1],
                [0, -1],
                [1, 0],
                [1, 1],
                [1, -1],
                [-1, 0],
                [-1, 1],
                [-1, -1],
            ]:
                ni = i + di
                nj = j + dj
                while (
                    0 <= ni < len(board)
                    and 0 <= nj < len(board[0])
                    and board[ni][nj] == "."
                ):
                    ni += di
                    nj += dj
                if (
                    0 <= ni < len(board)
                    and 0 <= nj < len(board[0])
                    and board[ni][nj] == "#"
                ):
                    n += 1
            if board[i][j] == "L":
                if n == 0:
                    t[i][j] = "#"
                    changes = 1
            elif board[i][j] == "#":
                if n > 4:
                    t[i][j] = "L"
                    changes = 1
    board = t

used = sum(sum(1 for i in r if i == "#") for r in board)
print("Part 2:", used)
