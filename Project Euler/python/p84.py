"""
In the game, Monopoly, the standard board is set up in the following way:

GO 	A1 CC1 A2 T1 R1 B1 CH1 B2  B3 JAIL
H2 	                              C1
T2 	  	                          U1
H1 	  	                          C2
CH3 	  	                      C3
R4 	  	                          R2
G3 	  	                          D1
CC3 	  	                      CC2
G2 	  	                          D2
G1 	  	                          D3
G2J F3 U2  F2 F1 R3 E3 E2  CH2 E1 FP

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance
 in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%.
 However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail,
if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll.
Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled.
When a player lands on CC or CH they take a card from the top of the respective pile and, after following the
instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile,
but for the purpose of this problem we are only concerned with cards that order a movement;
any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

    Community Chest (2/16 cards):
        Advance to GO
        Go to JAIL
    Chance (10/16 cards):
        Advance to GO
        Go to JAIL
        Go to C1
        Go to E3
        Go to H2
        Go to R1
        Go to next R (railway company)
        Go to next R
        Go to next U (utility company)
        Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square.
That is, the probability of finishing at that square after a roll. For this reason it should be clear that,
with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on
each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL,
and we shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to
produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10,
E3 (3.18%) = Square 24, and GO (3.09%) = Square 00.
So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""

"""
possible results for 2 4-sided dice
1 1: reroll
1 2: 3
1 3: 4
1 4: 5

2 1: 3
2 2: reroll
2 3: 5
2 4: 6

3 1: 4
3 2: 5
3 3: reroll
3 4: 7

4 1: 5
4 2: 6
4 3: 7
4 4: reroll
"""


# count all possible outcomes
odds = {}
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        r = a + b
                        if a == b:
                            r += c + d
                            if c == d:
                                r += e + f
                                if e == f:
                                    r = -1
                        odds[r] = odds.get(r, 0) + 1
# odds has the odds out of 16*16*16=4096 of getting that result from the dice, jail is -1

# redirecting squares
redirecting = {2: "CC", 7: "CH", 17: "CC", 22: "CH", 30: "GTJ", 33: "CC", 36: "CH"}

# odds of starting in any square, gets updated until stabilized
base = [1] * 40
base[30] = 0
for _ in range(10):
    # count the number of times we stop in each square
    stops = [0] * 40

    # for each start, find all possible ends
    # this assumes that we have equal chances for starting in any square, except for G2J
    for s in range(40):
        for k in odds:
            end = (s + k) % 40

            if k == -1:  # three doubles
                end = 30

            if end == 30:  # go to jail
                end = 10

            if end in [2, 17, 33]:  # community chest
                stops[0] += odds[k] * base[s]
                stops[10] += odds[k] * base[s]
                stops[end] += 14 * odds[k] * base[s]
            elif end in [7, 22, 36]:  # chance
                stops[0] += odds[k] * base[s]
                stops[10] += odds[k] * base[s]
                stops[11] += odds[k] * base[s]
                stops[24] += odds[k] * base[s]
                stops[39] += odds[k] * base[s]
                stops[5] += odds[k] * base[s]
                # next R
                if end == 7:
                    stops[15] += 2 * odds[k] * base[s]
                elif end == 22:
                    stops[25] += 2 * odds[k] * base[s]
                else:  # if end == 36:
                    stops[5] += 2 * odds[k] * base[s]
                # next U
                if end == 7:
                    stops[12] += odds[k] * base[s]
                elif end == 22:
                    stops[28] += odds[k] * base[s]
                else:  # if end == 36:
                    stops[12] += odds[k] * base[s]
                stops[end - 3] += odds[k] * base[s]
                stops[end] += 6 * odds[k] * base[s]
            else:
                stops[end] += 16 * odds[k] * base[s]

    s = float(sum(stops))
    for i in range(40):
        # print(i, stops[i], 100*stops[i]/s)
        base[i] = stops[i] / s

# print most stopped squares
for _ in range(3):
    m = max(stops)
    i = stops.index(m)
    print(i)
    stops[i] = 0
