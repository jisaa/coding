# coding: utf-8
"""
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin,
O(0,0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate
lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""

# using angles is useless because of precision issues
# using Pythagoras we work with integers only :)


def ds(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


m = 50 + 1
total = 0
for x in range(m):
    print(x)
    for y in range(m):
        if x == 0 == y:
            continue
        for p in range(m):
            for q in range(m):
                if p == q == 0:
                    continue
                if p == x and q == y:
                    continue
                a = [x, y]
                b = [p, q]
                c = [0, 0]

                d = ds(a, b)
                e = ds(b, c)
                f = ds(c, a)

                sides = sorted([d, e, f])
                if sides[0] + sides[1] == sides[2]:
                    total += 1

print("---")
print(total // 2)
