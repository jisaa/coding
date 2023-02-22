"""
Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
"""

ingredients = [[4, -2, 0, 0, 5], [0, 5, -1, 0, 8], [-1, 0, 5, 0, 6], [0, 0, -2, 2, 1]]


def f(ingredients, spoons):
    total = 1
    for x in range(4):
        s = 0
        for i in range(4):
            s += ingredients[i][x] * spoons[i]
        if s > 0:
            total *= s
    return total


def calories(ingredients, spoons):
    cals = 0
    for i in range(4):
        cals += ingredients[i][-1] * spoons[i]
    return cals


best = 0
best2 = 0
for a in range(100):
    for b in range(100 - a):
        for c in range(100 - a - b):
            d = 100 - a - b - c
            spoons = [a, b, c, d]
            t = f(ingredients, spoons)
            best = max(best, t)
            if calories(ingredients, spoons) == 500:
                best2 = max(best2, t)

print("Part 1:", best)
print("Part 2:", best2)
