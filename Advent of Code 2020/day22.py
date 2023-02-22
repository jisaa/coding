def loadDecks(deck1, deck2):
    d1 = True
    for line in open("inputs/day22.in"):
        line = line.strip()
        if "Player 2" in line:
            d1 = False
            continue
        if not line or "Player" in line:
            continue
        if d1:
            deck1.append(int(line))
        else:
            deck2.append(int(line))


def play(deck1, deck2):
    while deck1 and deck2:
        a = deck1.pop(0)
        b = deck2.pop(0)
        if a > b:
            deck1.append(a)
            deck1.append(b)
        else:
            deck2.append(b)
            deck2.append(a)
    if deck1:
        return deck1
    return deck2


def finalScore(deck):
    i = 1
    total = 0
    for c in deck[::-1]:
        total += i * c
        i += 1
    return total


deck1 = []
deck2 = []
loadDecks(deck1, deck2)
print("Part 1:", finalScore(play(deck1, deck2)))


def playRecursive(deck1, deck2, s={}):
    seen = set()
    start = (tuple(deck1), tuple(deck2))
    if start in s:
        return s[start]
    while deck1 and deck2:
        t = (tuple(deck1), tuple(deck2))
        if t in seen:
            s[t] = (deck1, 1)
            s[start] = (deck1, 1)
            return deck1, 1
        if t in s:
            return s[t]
        seen.add(t)
        a = deck1.pop(0)
        b = deck2.pop(0)
        if a <= len(deck1) and b <= len(deck2):
            d, w = playRecursive(deck1[:a], deck2[:b])
            if w == 1:
                deck1.append(a)
                deck1.append(b)
            else:
                deck2.append(b)
                deck2.append(a)
        elif a > b:
            deck1.append(a)
            deck1.append(b)
        else:
            deck2.append(b)
            deck2.append(a)
    if deck1:
        s[start] = (deck1, 1)
        return deck1, 1
    s[start] = (deck2, 2)
    return deck2, 2


deck1 = []
deck2 = []
loadDecks(deck1, deck2)
print("Part 2:", finalScore(playRecursive(deck1, deck2)[0]))
