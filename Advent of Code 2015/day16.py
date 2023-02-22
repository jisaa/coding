class Sue:
    def __init__(self):
        self.id = -1
        self.children = 3
        self.cats = 7
        self.samoyeds = 2
        self.pomeranians = 3
        self.akitas = 0
        self.vizslas = 0
        self.goldfish = 5
        self.trees = 3
        self.cars = 2
        self.perfumes = 1

    def match(self, other):
        if other.children not in [-1, self.children]:
            return False
        if other.cats not in [-1, self.cats]:
            return False
        if other.samoyeds not in [-1, self.samoyeds]:
            return False
        if other.pomeranians not in [-1, self.pomeranians]:
            return False
        if other.akitas not in [-1, self.akitas]:
            return False
        if other.vizslas not in [-1, self.vizslas]:
            return False
        if other.goldfish not in [-1, self.goldfish]:
            return False
        if other.trees not in [-1, self.trees]:
            return False
        if other.cars not in [-1, self.cars]:
            return False
        if other.perfumes not in [-1, self.perfumes]:
            return False
        return True

    def match2(self, other):
        if other.children not in [-1, self.children]:
            return False
        if other.cats != -1 and other.cats <= self.cats:
            return False
        if other.samoyeds not in [-1, self.samoyeds]:
            return False
        if other.pomeranians != -1 and other.pomeranians >= self.pomeranians:
            return False
        if other.akitas not in [-1, self.akitas]:
            return False
        if other.vizslas not in [-1, self.vizslas]:
            return False
        if other.goldfish != -1 and other.goldfish >= self.goldfish:
            return False
        if other.trees != -1 and other.trees <= self.trees:
            return False
        if other.cars not in [-1, self.cars]:
            return False
        if other.perfumes not in [-1, self.perfumes]:
            return False
        return True

    def load(self, line):
        _, n, rest = line.split(" ", 2)
        self.id = int(n[:-1])
        self.children = -1
        self.cats = -1
        self.samoyeds = -1
        self.pomeranians = -1
        self.akitas = -1
        self.vizslas = -1
        self.goldfish = -1
        self.trees = -1
        self.cars = -1
        self.perfumes = -1
        for t in rest.split(", "):
            thing, n = t.split(": ")
            n = int(n)
            if thing == "children":
                self.children = n
            if thing == "cats":
                self.cats = n
            if thing == "samoyeds":
                self.samoyeds = n
            if thing == "pomeranians":
                self.pomeranians = n
            if thing == "akitas":
                self.akitas = n
            if thing == "vizslas":
                self.vizslas = n
            if thing == "goldfish":
                self.goldfish = n
            if thing == "trees":
                self.trees = n
            if thing == "cars":
                self.cars = n
            if thing == "perfumes":
                self.perfumes = n


sender = Sue()
t = Sue()

for line in open("inputs/day16.in"):
    t.load(line.strip())
    if sender.match(t):
        print("Part 1:", t.id)
    if sender.match2(t):
        print("Part 2:", t.id)
