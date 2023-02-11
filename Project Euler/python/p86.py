# encoding: utf-8
"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner.
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions,
up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100.
This is the least value of M for which the number of solutions first exceeds two thousand;
the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.


Brute forcing:
M = 799  ->  174,583 solutions
M = 999  ->  280,308 solutions
M = 1499 ->  666,057 solutions
M = 1799 ->  977,031 solutions
M = 1817 ->  999,850 solutions
M = 1818 -> 1,000,457 solutions
M = 1819 -> 1,000,457 solutions
M = 1825 -> 1,014,222 solutions
M = 1849 -> 1,046,353 solutions
"""

import gmpy

# a bit slow, but does the job
M = 1819
n = 0
for a in range(1, M):
    print(a)
    for b in range(a, M):
        for c in range(b, M):
            n += gmpy.is_square((a + b) ** 2 + c**2)
print("Total:", n)


# check which combination gives the lowest distance,
# given that a <= b <= c
# d = {'x': 4455100, 'y': 0, 'z': 0, 't': 44850, 'tx': 44850, 'ty': 44850, 'tz': 299}
"""
M = 300
d = {c:0 for c in 'x y z t tx ty tz'.split()}
n = 0
for a in range(1, M):
    #print(a)
    for b in range(a, M):
        for c in range(b, M):
            x = (a+b)**2 + c**2
            y = (a+c)**2 + b**2
            z = (c+b)**2 + a**2
            if z>x<y:
                d['x'] += 1
            elif x>y<z:
                d['y'] += 1
            elif x>z<y:
                d['z'] += 1
            else:
                if z>=x<=y:
                    d['tx'] += 1
                if x>=y<=z:
                    d['ty'] += 1
                if x>=z<=y:
                    d['tz'] += 1
                d['t'] += 1
            n += gmpy.is_square(min(x, y, z))
print('Total:', n)
print(d)
"""
