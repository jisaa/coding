"""
An ant moves on a regular grid of squares that are coloured either black or white.
The ant is always oriented in one of the cardinal directions (left, right, up or down) and moves from square to
adjacent square according to the following rules:
- if it is on a black square, it flips the color of the square to white,
  rotates 90 degrees counterclockwise and moves forward one square.
- if it is on a white square, it flips the color of the square to black,
  rotates 90 degrees clockwise and moves forward one square.

Starting with a grid that is entirely white, how many squares are black after 10^18 moves of the ant?
"""

# from simulation, at 11,000 steps there are 834 black squares
steps = 11000
blacks = 834
# every 104 steps, +12 black cells, there are 64 steps left to get the total, which add 10 extra black squares
print(blacks + 12 * ((10**18 - steps) / 104) + 10)
exit()

# simulation and plot to find a pattern
from matplotlib import pyplot

blacks = []
x = y = 0
direction = "right"
steps = 0
while steps < 11064:
    steps += 1
    if (x, y) in blacks:
        blacks.remove((x, y))
        if direction == "right":
            direction = "up"
        elif direction == "up":
            direction = "left"
        elif direction == "left":
            direction = "down"
        else:
            direction = "right"
    else:
        blacks.append((x, y))
        if direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        elif direction == "left":
            direction = "up"
        else:
            direction = "right"
    if direction == "right":
        x += 1
    elif direction == "up":
        y += 1
    elif direction == "left":
        x -= 1
    else:
        y -= 1
    # print(steps, blacks)

print(len(blacks), steps)

cx = [p[0] for p in blacks]
cy = [p[1] for p in blacks]

pyplot.plot(cx, cy, "o")
pyplot.axis([min(cx) - 1, max(cx) + 1, min(cy) - 1, max(cy) + 1])
pyplot.axis("equal")
pyplot.show()
