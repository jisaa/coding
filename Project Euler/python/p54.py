# encoding: utf-8
"""


In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand    Player 1	 	    Player 2	 	    Winner
1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
        Pair of Fives       Pair of Eights

2	 	5D 8C 9S JS AC	 	2C 5C 7D 8S QH      Player 1
        Highest card Ace    Highest card Queen

3	 	2D 9C AS AH AC	 	3D 6D 7D TD QD      Player 2
        Three Aces          Flush with Diamonds

4	 	4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven

5	 	2H 2D 4C 4D 4S	 	3C 3D 3S 9S 9D      Player 1
        Full House          Full House
        With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""


class Hand:
    def __init__(self, string):
        self.cards = string.split()
        self.values = []
        for v in [c[0] for c in self.cards]:
            if v == "T":
                self.values.append(8)
            elif v == "J":
                self.values.append(9)
            elif v == "Q":
                self.values.append(10)
            elif v == "K":
                self.values.append(11)
            elif v == "A":
                self.values.append(12)
            else:
                self.values.append(int(v) - 2)
        self.values.sort()
        self.counts = [self.values.count(v) for v in self.values]

    def all_same_suit(self):
        return all(i[1] == self.cards[0][1] for i in self.cards)

    def __repr__(self):
        return " ".join(self.cards)

    def score(self):
        """
        Name                Description                                     Score range
        High Card:          Highest value card.                             highest value, 0 - 12
        One Pair:           Two cards of the same value.                    12 + pair value + highest other/12
        Two Pairs:          Two different pairs.                            24 + highest pair value
                                                                               + lowest pair value/12
                                                                               + highest other/144
        Three of a Kind:    Three cards of the same value.                  36 + trio value + highest other/12
        Straight:           All cards are consecutive values.               48 + highest value
        Flush:              All cards of the same suit.                     60 + highest value
        Full House:         Three of a kind and a pair.                     72 + trio value + pair value/12
        Four of a Kind:     Four cards of the same value.                   84 + poker value
        Straight Flush:     All cards are consecutive values of same suit.  96 + highest value
        Royal Flush:        Ten, Jack, Queen, King, Ace, in same suit.      96 + highest value
        """

        # Straight/Royal Flush
        if self.all_same_suit() and all(
            self.values[i] + 1 == self.values[i + 1] for i in range(4)
        ):
            return 96 + self.values[-1]
        # Four of a Kind
        if 4 in self.counts:
            return 84 + (
                self.values[0] if self.values[0] == self.values[1] else self.values[-1]
            )
        # Full House
        if 3 in self.counts and 2 in self.counts:
            t = self.values[self.counts.index(3)]
            p = self.values[self.counts.index(2)]
            return 72 + t + p / 12.0
        # Flush
        if self.all_same_suit():
            return 60 + self.values[-1]
        # Straight
        if all(self.values[i] + 1 == self.values[i + 1] for i in range(4)):
            return 48 + self.values[-1]
        # Three of a Kind
        if 3 in self.counts:
            t = self.values[self.counts.index(3)]
            i = 4
            while self.counts[i] == 3:
                i -= 1
            b = self.values[i]
            return 36 + t + b / 12.0
        # Two Pairs
        if self.counts.count(2) == 4:
            low_pair = self.values[self.counts.index(2)]
            high_pair = self.values[self.counts.index(2, self.counts.index(2) + 2)]
            other = self.values[self.counts.index(1)]
            return 24 + high_pair + low_pair / 12.0 + other / 144.0
        # One Pair
        if 2 in self.counts:
            p = self.values[self.counts.index(2)]
            i = 4
            while self.counts[i] == 2:
                i -= 1
            b = self.values[i]
            return 12 + p + b / 12.0
        # High Card
        return self.values[-1]


count = 0
with open("inputs/p54.in") as f:
    for line in f:
        hand1 = Hand(line[:14])
        hand2 = Hand(line[15:-1])
        if hand1.score() > hand2.score():
            count += 1
print(count)
