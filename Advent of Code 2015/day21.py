# cost, damage, armor
weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

armors = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]

rings = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]


def will_player_win(weapon, armor, ring1, ring2):
    boss_hp = 100
    boss_damage = 8
    boss_armor = 2

    player_hp = 100
    player_damage = weapon[1] + ring1[1] + ring2[1]
    player_armor = armor[2] + ring1[2] + ring2[2]

    turn = "player"
    while 1:
        if boss_hp <= 0:
            return True
        if player_hp <= 0:
            return False
        if turn == "player":
            turn = "boss"
            boss_hp -= max(1, player_damage - boss_armor)
        else:
            turn = "player"
            player_hp -= max(1, boss_damage - player_armor)


# the inventory is small, brute force all combinations
best_cost = sum(e[0] for e in armors + weapons + rings)
worst_cost = 0
for armor in armors:
    for weapon in weapons:
        for ring1 in rings:
            for ring2 in rings:
                if ring2 == ring1 and ring1 != (0, 0, 0):
                    continue
                cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
                if will_player_win(weapon, armor, ring1, ring2):
                    best_cost = min(best_cost, cost)
                else:
                    worst_cost = max(worst_cost, cost)
print("Part 1:", best_cost)
print("Part 2:", worst_cost)
