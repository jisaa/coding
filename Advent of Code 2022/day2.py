f = open("inputs/day2.in")

score = 0
score2 = 0
for line in f:
    other, me = line.split()
    score += {"X": 1, "Y": 2, "Z": 3}[me]
    if me + other in "XC YA ZB":
        # I win
        score += 6
    elif me + other in "XA YB ZC":
        # tie
        score += 3

    if me == "X":
        # need to lose
        pick = {"A": "Z", "B": "X", "C": "Y"}[other]
    elif me == "Y":
        # need to draw
        pick = {"A": "X", "B": "Y", "C": "Z"}[other]
        score2 += 3
    else:
        # need to win
        pick = {"A": "Y", "B": "Z", "C": "X"}[other]
        score2 += 6
    score2 += {"X": 1, "Y": 2, "Z": 3}[pick]

print("Part 1:", score)
print("Part 2:", score2)
