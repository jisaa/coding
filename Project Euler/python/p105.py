# coding: utf-8
"""
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two
non-empty disjoint subsets, B and C, the following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84,
whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations
and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven
to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets,
 A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to Problem 103 and Problem 106.
"""


def partition(collection):
    if len(collection) == 1:
        yield [collection]
        return
    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n + 1 :]
        # put `first` in its own subset
        yield [[first]] + smaller


def is_special(a):
    if len(set(a)) != len(a):
        return False
    a = sorted(a)
    # double check, but speeds things up
    if a[0] + a[1] <= a[-1]:
        return False
    for p in partition(a):
        if len(p) > 1:
            for i in range(len(p)):
                for j in range(i + 1, len(p)):
                    if sum(p[i]) == sum(p[j]):
                        return False
                    if len(p[i]) > len(p[j]) and sum(p[j]) > sum(p[i]):
                        return False
                    if len(p[j]) > len(p[i]) and sum(p[i]) > sum(p[j]):
                        return False
    return True


total = 0
k = 0
with open("inputs/p105.in") as f:
    for line in f:
        print(k)
        k += 1
        t = [int(i) for i in line.strip().split(",")]
        if is_special(t):
            total += sum(t)
print(total)
