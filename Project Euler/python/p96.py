"""

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar,
and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles,
however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column,
and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting
puzzle grid and its solution grid.

0 0 3 	0 2 0 	6 0 0
9 0 0   3 0 5   0 0 1
0 0 1   8 0 6   4 0 0

0 0 8 	1 0 2 	9 0 0
7 0 0   0 0 0   0 0 8
0 0 6   7 0 8   2 0 0

0 0 2 	6 0 9 	5 0 0
8 0 0   2 0 3   0 0 9
0 0 5   0 1 0   3 0 0


4 8 3 	9 2 1 	6 5 7
9 6 7   3 4 5   8 2 1
2 5 1   8 7 6   4 9 3

5 4 8 	1 3 2 	9 7 6
7 2 9   5 6 4   1 3 8
1 3 6   7 9 8   2 4 5

3 7 2 	6 8 9 	5 1 4
8 1 4   2 5 3   7 6 9
6 9 5   4 1 7   3 8 2

A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
although it may be necessary to employ "guess and test" methods in order to eliminate options
(there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle;
the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""

total = 0
with open("inputs/p96.in") as f:
    square = [[0, 1, 2]] * 3 + [[3, 4, 5]] * 3 + [[6, 7, 8]] * 3
    for _ in range(50):
        print(f.readline().strip() + ":", end="")
        m = []
        for __ in range(9):
            m.append([int(i) for i in f.readline().strip()])

        possibles = []
        for __ in range(9):
            possibles.append([])
            for ___ in range(9):
                possibles[-1].append(list(range(1, 10)))
        for i in range(9):
            for j in range(9):
                if m[i][j]:
                    possibles[i][j] = [m[i][j]]
        # don't need to solve completely

        count = 0
        while any(0 in r for r in m):
            count += 1
            if count > 100:
                break

            # for row in m:
            #     print row
            # print '---'

            # add numbers
            for i in range(9):
                for j in range(9):
                    # only possible one
                    if len(possibles[i][j]) == 1:
                        m[i][j] = possibles[i][j][0]
                    elif len(possibles[i][j]) > 1:
                        # check if any value is not possible for same row, col or square
                        for v in possibles[i][j]:
                            singleCol = True
                            singleRow = True
                            singleSquare = True

                            for k in range(9):
                                # rows
                                if k != j and v in possibles[i][k]:
                                    singleRow = False
                                # columns
                                if k != i and v in possibles[k][j]:
                                    singleCol = False
                            for p in square[i]:
                                for q in square[j]:
                                    if (i != p or j != q) and v in possibles[p][q]:
                                        singleSquare = False
                            if singleCol or singleRow or singleSquare:
                                m[i][j] = v
                                possibles[i][j] = [m[i][j]]
                                break

            # discard used
            for i in range(9):
                for j in range(9):
                    if m[i][j]:
                        for k in range(9):
                            # rows
                            if j != k and m[i][j] in possibles[i][k]:
                                possibles[i][k].remove(m[i][j])
                            # columns
                            if i != k and m[i][j] in possibles[k][j]:
                                possibles[k][j].remove(m[i][j])
                        # squares

                        for p in square[i]:
                            for q in square[j]:
                                if (i != p or j != q) and m[i][j] in possibles[p][q]:
                                    possibles[p][q].remove(m[i][j])
            # discard impossibles
            # for each square, if there is a possible number that appears only in a single row
            # discard appearances of that number from the same row in other squares
            for s in range(9):
                pass

        if 0 in m[0][:3]:
            print("unsolved")
            for i in range(9):
                t = [str(v) for v in m[i]]
                for j in range(9):
                    if t[j] == "0":
                        t[j] = ""
                print(
                    "\t".join(t[:3])
                    + "\t|\t"
                    + "\t".join(t[3:6])
                    + "\t|\t"
                    + "\t".join(t[6:])
                )
                if i in [2, 5]:
                    print("\t".join(list("---+---+---")))
            continue
            for i in range(9):
                for j in range(9):
                    print(i, j, possibles[i][j])
        else:
            t = int("".join(str(i) for i in m[0][:3]))
            print(t)
            total += t

print(total)
