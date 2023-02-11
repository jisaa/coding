# encoding: utf-8

"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
"""

import itertools


def value(n):
    l1 = [n[0], n[2], n[4]]
    return sum(l1) if sum(l1) > 9 else " " + str(sum(l1))


def validate(n):
    l1 = [n[0], n[2], n[4]]
    l2 = [n[1], n[4], n[7]]
    l3 = [n[8], n[7], n[6]]
    l4 = [n[9], n[6], n[3]]
    l5 = [n[5], n[3], n[2]]
    return sum(l1) == sum(l2) == sum(l3) == sum(l4) == sum(l5)


def show(n):
    l1 = [n[0], n[2], n[4]]
    l2 = [n[1], n[4], n[7]]
    l3 = [n[8], n[7], n[6]]
    l4 = [n[9], n[6], n[3]]
    l5 = [n[5], n[3], n[2]]
    return (
        "".join(str(i) for i in l1)
        + "".join(str(i) for i in l2)
        + "".join(str(i) for i in l3)
        + "".join(str(i) for i in l4)
        + "".join(str(i) for i in l5)
    )


def areTheSame(x, y):
    l1x = [x[0], x[2], x[4]]
    l2x = [x[1], x[4], x[7]]
    l3x = [x[8], x[7], x[6]]
    l4x = [x[9], x[6], x[3]]
    l5x = [x[5], x[3], x[2]]
    l1y = [y[0], y[2], y[4]]
    l2y = [y[1], y[4], y[7]]
    l3y = [y[8], y[7], y[6]]
    l4y = [y[9], y[6], y[3]]
    l5y = [y[5], y[3], y[2]]
    ly = [l1y, l2y, l3y, l4y, l5y]
    return l1x in ly and l2x in ly and l3x in ly and l4x in ly and l5x in ly


n = range(1, 11)
x = itertools.permutations(n)
valid = []
for p in x:
    if validate(p):
        isNew = True
        for i in valid:
            if areTheSame(i, p):
                isNew = False
                break
        if isNew:
            valid.append(p)
for p in valid:
    print(value(p), show(p))

print(show(valid[-1]))
