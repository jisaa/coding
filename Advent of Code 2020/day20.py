raw_tiles = []
ids = []

t = []
for line in open("inputs/day20.in"):
    line = line.strip()
    if "Tile" in line:
        ids.append(int(line.split()[1][:-1]))
        if t:
            raw_tiles.append(t)
            t = []
    elif line:
        t += (line,)
raw_tiles.append(t)


class Tile:
    def __init__(self, tile, id):
        self.id = id
        self.top = list(tile[0])
        self.bottom = list(tile[-1])
        self.left = [t[0] for t in tile]
        self.right = [t[-1] for t in tile]
        self.image = []
        for r in tile[1:-1]:
            self.image.append(r[1:-1])

    def flip(self):
        self.left, self.right = self.right, self.left
        self.top = self.top[::-1]
        self.bottom = self.bottom[::-1]
        for i in range(len(self.image)):
            self.image[i] = self.image[i][::-1]

    def rotate(self):
        t = self.left
        self.left = self.top[::-1]
        self.top = self.right
        self.right = self.bottom[::-1]
        self.bottom = t

        t = []
        for _ in self.image:
            t += ([],)
        for r in self.image:
            for j in range(len(r)):
                t[-j - 1].append(r[j])
        self.image = t

    def p(self):
        print("".join(self.top))
        for i in range(1, len(self.left) - 1):
            print(self.left[i], "      ", self.right[i])
        print("".join(self.bottom))

    def mark_right(self):
        self.mem = self.top[2], self.left[2], self.bottom[2]
        self.top[2] = "x"
        self.left[2] = "x"
        self.bottom[2] = "x"

    def unmark_right(self):
        self.top[2] = self.mem[0]
        self.left[2] = self.mem[1]
        self.bottom[2] = self.mem[2]

    def mark_bottom(self):
        self.mem = self.top[2], self.left[2], self.right[2]
        self.top[2] = "x"
        self.left[2] = "x"
        self.right[2] = "x"

    def unmark_bottom(self):
        self.top[2] = self.mem[0]
        self.left[2] = self.mem[1]
        self.right[2] = self.mem[2]


def can_fit(a, b):
    return (
        a.left == b.right or a.right == b.left or a.top == b.bottom or a.bottom == b.top
    )


def can_fit_somehow(a, b):
    for _ in range(4):
        if can_fit(a, b):
            return True
        b.rotate()
    b.flip()
    for _ in range(4):
        if can_fit(a, b):
            return True
        b.rotate()
    return False


tiles = [Tile(t, i) for t, i in zip(raw_tiles, ids)]

fit = [0] * len(tiles)

for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        if can_fit_somehow(tiles[i], tiles[j]):
            fit[i] += 1
            fit[j] += 1

total = 1
for i in range(len(fit)):
    if fit[i] == 2:
        total *= ids[i]
print("Part 1:", total)


used = [0] * len(tiles)
i = fit.index(2)
used[i] = 1
image_tiles = []
t = [i]

tiles[i].mark_right()

size = int(len(tiles) ** 0.5)
while not all(used):
    for i in range(len(tiles)):
        if used[i]:
            continue
        fits = True
        if len(image_tiles) > 0:
            fits = fits and can_fit_somehow(tiles[image_tiles[-1][len(t)]], tiles[i])
        if len(t) > 0:
            fits = fits and can_fit_somehow(tiles[t[-1]], tiles[i])
        if fits:
            t.append(i)
            used[i] = True
            tiles[i].mark_right()
            break
    if len(t) == size:
        image_tiles.append(t)
        for i in t:
            tiles[i].unmark_right()
            tiles[i].mark_bottom()
        t = []

for r in image_tiles:
    for i in r:
        tiles[i].unmark_bottom()

full_image = []
for row in image_tiles:
    for x in range(len(tiles[0].image)):
        t = ""
        for i in row:
            t += "".join(tiles[i].image[x])
        full_image.append(t)

moster = [
    # 0123456789 123456789
    "                  # "
    "#    ##    ##    ###"
    " #  #  #  #  #  #   "
]


def full_flip():
    for i in range(len(full_image)):
        full_image[i] = full_image[i][::-1]


def full_rotate():
    t = []
    for _ in full_image:
        t += ([],)
    for r in full_image:
        for j in range(len(r)):
            t[-j - 1].append(r[j])
    return t


def has_monster(image, x, y):
    deltas = (
        (0, 18),
        (1, 0),
        (1, 5),
        (1, 6),
        (1, 11),
        (1, 12),
        (1, 17),
        (1, 18),
        (1, 19),
        (2, 1),
        (2, 4),
        (2, 7),
        (2, 10),
        (2, 13),
        (2, 16),
    )
    try:
        return all(image[x + dx][y + dy] == "#" for (dx, dy) in deltas)
    except:
        return False


full_flip()
full_image = full_rotate()
n_monsters = 0
for i in range(len(full_image)):
    for j in range(len(full_image[0])):
        if has_monster(full_image, i, j):
            n_monsters += 1

np = sum(r.count("#") for r in full_image)

print("Part 2:", np - 15 * n_monsters)
