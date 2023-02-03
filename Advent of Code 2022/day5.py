""" harcoded this part of the input
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
"""

stacks = {
    "1": list("BQC"),
    "2": list("RQWZ"),
    "3": list("BMRLV"),
    "4": list("CZHVTW"),
    "5": list("DZHBNVG"),
    "6": list("HNPCJFVQ"),
    "7": list("DGTRWZS"),
    "8": list("CGMNBWZP"),
    "9": list("NJBMWQFP"),
}

stacks2 = {
    "1": list("BQC"),
    "2": list("RQWZ"),
    "3": list("BMRLV"),
    "4": list("CZHVTW"),
    "5": list("DZHBNVG"),
    "6": list("HNPCJFVQ"),
    "7": list("DGTRWZS"),
    "8": list("CGMNBWZP"),
    "9": list("NJBMWQFP"),
}

f = open("inputs/day5.in")
for line in f:
    # move 3 from 6 to 2
    _, n, _, a, _, b = line.strip().split()
    n = int(n)
    stacks[b] += stacks[a][-n:][::-1]
    stacks[a] = stacks[a][:-n]
    stacks2[b] += stacks2[a][-n:]
    stacks2[a] = stacks2[a][:-n]

top = ""
for i in "123456789":
    top += stacks[i][-1]
print("Part 1:", top)

top2 = ""
for i in "123456789":
    top2 += stacks2[i][-1]
print("Part 2:", top2)
