"""
A square is drawn around a circle as shown in the diagram below on the left.
We shall call the blue shaded region the L-section.
A line is drawn from the bottom left of the square to the top right as shown in the diagram on the right.
We shall call the orange shaded region a concave triangle.
p587_concave_triangle_1.png

It should be clear that the concave triangle occupies exactly half of the L-section.

Two circles are placed next to each other horizontally, a rectangle is drawn around both circles, and a line is drawn from the bottom left to the top right as shown in the diagram below.
p587_concave_triangle_2.png

This time the concave triangle occupies approximately 36.46% of the L-section.

If n circles are placed next to each other horizontally, a rectangle is drawn around the n circles, and a line is drawn from the bottom left to the top right, then it can be shown that the least value of n for which the concave triangle occupies less than 10% of the L-section is n = 15.

What is the least value of n for which the concave triangle occupies less than 0.1% of the L-section?
"""


from math import pi, sqrt, asin

blue_area = (4 - pi) / 4

n = 14
ratio = 0.5
while ratio > 0.001:
    # get intersection between line and circle
    # circle: (x-1)**2 + (y-1)**2 = 1
    # line:   y = x/n
    x = n * (n - sqrt(2 * n) + 1) / (n * n + 1)
    y = x / n

    # get triangle area
    triangle_area = x * y / 2
    # get area under circle
    integral = lambda x: -((x - 1) * sqrt(-x * (x - 2)) - 2 * x + asin(x - 1)) / 2
    circle_area = integral(1) - integral(x)
    orange_area = triangle_area + circle_area
    ratio = orange_area / blue_area
    print(n, ratio)
    n += 1

print(n, ratio)
