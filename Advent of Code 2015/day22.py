import random


class Game:
    def __init__(
        self, player_hp=50, player_mana=500, boss_hp=55, boss_damage=8, hard=False
    ):
        self.log = []
        self.hard = hard
        self.player_turn = True
        self.active_effects = {
            "shield": 0,
            "poison": 0,
            "recharge": 0,
        }

        self.player_hp = player_hp
        self.player_armor = 0
        self.player_mana = player_mana
        self.spent_mana = 0
        # puzzle input
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage

    def game_turn(self):
        if self.hard and self.player_turn:
            self.player_hp -= 1
        # apply ongoing effects and decrease effect timers
        if self.active_effects["shield"] > 1:
            self.player_armor = 7
            self.active_effects["shield"] -= 1
        else:
            self.player_armor = 0
        if self.active_effects["poison"] > 0:
            self.active_effects["poison"] -= 1
            self.boss_hp -= 3
        if self.active_effects["recharge"] > 0:
            self.player_mana += 101
            self.active_effects["recharge"] -= 1

        if self.boss_hp <= 0:
            return
        if self.player_hp <= 0:
            return

        if self.player_turn:
            # choose spell to cast
            spells = [
                # cost, name
                (53, "magic missile"),
                (73, "drain"),
                (113, "shield"),
                (173, "poison"),
                (229, "recharge"),
            ]
            # filter by available mana
            can_cast = [s for s in spells if s[0] <= self.player_mana]
            # filter by active effects
            can_cast = [s for s in can_cast if self.active_effects.get(s[1], 0) == 0]
            try:
                spell = random.choice(can_cast)
            except:
                self.player_hp = 0
                return
            # cast spell
            self.log.append(spell[1])
            self.player_mana -= spell[0]
            self.spent_mana += spell[0]
            if spell[1] == "magic missile":
                self.boss_hp -= 4
            elif spell[1] == "drain":
                self.boss_hp -= 2
                self.player_hp += 2
            elif spell[1] == "shield":
                self.active_effects["shield"] = 6
            elif spell[1] == "poison":
                self.active_effects["poison"] = 6
            elif spell[1] == "recharge":
                self.active_effects["recharge"] = 5
            # pass turn over
            self.player_turn = False
        else:
            # apply damage
            self.player_hp -= max(1, self.boss_damage - self.player_armor)
            # pass turn over
            self.player_turn = True

    def pprint(self):
        print(f"Player: {self.player_hp} hp {self.player_mana} mana")
        print(f"Boss: {self.boss_hp} hp")


# just simulate a large number of games choosing random spells
for i, hard in enumerate([False, True]):
    best = 999999
    for _ in range(99999):
        g = Game(hard=hard)
        while g.player_hp > 0 and g.boss_hp > 0:
            g.game_turn()
        if g.player_hp > 0 and g.spent_mana < best:
            best = g.spent_mana

    print(f"Part {i+1}:", best)
