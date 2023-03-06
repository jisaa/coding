class State:
    def __init__(self) -> None:
        self.time = 0
        self.ore_robots = 1
        self.clay_robots = 0
        self.obsidian_robots = 0
        self.geode_robots = 0
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0

    def __repr__(self) -> str:
        s = f"time: {self.time}, "
        s += f"robots: {self.ore_robots}, {self.clay_robots}, {self.obsidian_robots}, {self.geode_robots}, "
        s += f"resources: {self.ore}, {self.clay}, {self.obsidian}, {self.geode}"
        return s

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return (
            self.time == other.time
            and self.ore_robots == other.ore_robots
            and self.clay_robots == other.clay_robots
            and self.obsidian_robots == other.obsidian_robots
            and self.geode_robots == other.geode_robots
            and self.ore == other.ore
            and self.clay == other.clay
            and self.obsidian == other.obsidian
            and self.geode == other.geode
        )

    def __hash__(self):
        return hash(str(self))

    def copy(self):
        n = State()
        n.time = self.time
        n.ore_robots = self.ore_robots
        n.clay_robots = self.clay_robots
        n.obsidian_robots = self.obsidian_robots
        n.geode_robots = self.geode_robots
        n.ore = self.ore
        n.clay = self.clay
        n.obsidian = self.obsidian
        n.geode = self.geode
        return n

    def lazy_next(self):
        n = self.copy()
        n.time += 1
        n.ore += n.ore_robots
        n.clay += n.clay_robots
        n.obsidian += n.obsidian_robots
        n.geode += n.geode_robots
        return n

    # returns list of [n_ore_robots, n_clay_robots, n_obsidian_robots, n_geode_robots]
    # where each number is the amount of robots that can be bought for next round
    def can_buy(self, blueprint):
        options = [[0, 0, 0, 0]]
        if self.ore >= blueprint.ore_price[0]:
            options.append([self.ore // blueprint.ore_price[0], 0, 0, 0])
        if self.ore >= blueprint.clay_price[0]:
            options.append([0, self.ore // blueprint.clay_price[0], 0, 0])
        if (
            self.ore >= blueprint.obsidian_price[0]
            and self.clay >= blueprint.obsidian_price[1]
        ):
            n = min(
                self.ore // blueprint.obsidian_price[0],
                self.clay // blueprint.obsidian_price[1],
            )
            options.append([0, 0, n, 0])
        if (
            self.ore >= blueprint.geode_price[0]
            and self.obsidian >= blueprint.geode_price[2]
        ):
            n = min(
                self.ore // blueprint.geode_price[0],
                self.obsidian // blueprint.geode_price[2],
            )
            options.append([0, 0, 0, n])
        return options

    def next_states(self, blueprint):
        if self.time == 24:
            return []
        new_states = []
        for buy_options in self.can_buy(blueprint):
            n = self.lazy_next()
            # add robots
            n.ore_robots += buy_options[0]
            n.clay_robots += buy_options[1]
            n.obsidian_robots += buy_options[2]
            n.geode_robots += buy_options[3]
            # spend resources
            n.ore -= buy_options[0] * blueprint.ore_price[0]
            n.ore -= buy_options[1] * blueprint.clay_price[0]
            n.ore -= buy_options[2] * blueprint.obsidian_price[0]
            n.ore -= buy_options[3] * blueprint.geode_price[0]
            n.clay -= buy_options[0] * blueprint.ore_price[1]
            n.clay -= buy_options[1] * blueprint.clay_price[1]
            n.clay -= buy_options[2] * blueprint.obsidian_price[1]
            n.clay -= buy_options[3] * blueprint.geode_price[1]
            n.obsidian -= buy_options[0] * blueprint.ore_price[2]
            n.obsidian -= buy_options[1] * blueprint.clay_price[2]
            n.obsidian -= buy_options[2] * blueprint.obsidian_price[2]
            n.obsidian -= buy_options[3] * blueprint.geode_price[2]
            new_states.append(n)

        return new_states


class Blueprint:
    def __init__(self, id, ore_price, clay_price, obsidian_price, geode_price) -> None:
        self.id = id
        self.ore_price = ore_price
        self.clay_price = clay_price
        self.obsidian_price = obsidian_price
        self.geode_price = geode_price

    def quality(self):
        return self.id * self.max_geodes()

    # too slow :(
    def max_geodes(self):
        q = [State()]
        best = 0
        i = 0
        seen = set(q)
        skipped = 0
        while q:
            i += 1
            if i % 1000000 == 0:
                print(i, len(q), q)
            q.sort(key = lambda s:s.geode)
            state = q.pop()
            if state.geode > best:
                best = state.geode
                print(self.id, best, len(q))
            for s in state.next_states(self):
                if s not in seen:
                    q.append(s)
                    seen.add(s)
                else:
                    skipped += 1
                    if skipped%100000 == 0:
                        print('skipped', skipped)
        return best


blueprints = []
for line in open("inputs/day19.in").readlines():
    words = line.split()
    id = int(words[1][:-1])
    # costs as arrays of [ore, clay, obsidian]
    ore_price = [int(words[6]), 0, 0]
    clay_price = [int(words[12]), 0, 0]
    obsidian_price = [int(words[18]), int(words[21]), 0]
    geode_price = [int(words[27]), 0, int(words[30])]

    blueprints.append(Blueprint(id, ore_price, clay_price, obsidian_price, geode_price))

print("Part 1:", sum(b.quality() for b in blueprints))
