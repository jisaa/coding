# example values
tx1 = 20
tx2 = 30
ty1 = -10
ty2 = -5
# input values
tx1 = 60
tx2 = 94
ty1 = -171
ty2 = -136


class Probe:
    def __init__(self, vx, vy):
        self.x = 0
        self.y = 0
        self.vx = vx
        self.vy = vy

    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.vx > 0:
            self.vx -= 1
        elif self.vx < 0:
            self.vx += 1
        self.vy -= 1

    def is_in_target_area(self):
        return tx1 <= self.x <= tx2 and ty1 <= self.y <= ty2


valid_speeds = 0
for vx in range(1, tx2 + 10):
    for vy in range(ty1 - 10, -ty1 + 10):
        p = Probe(vx, vy)
        for _steps in range(999):
            p.step()
            if p.is_in_target_area():
                valid_speeds += 1
                break
print("Part 2:", valid_speeds)
