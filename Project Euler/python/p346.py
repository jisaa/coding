"""
The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6
(i.e. 710 = 116 = 1112). In other words, 7 is a repunit in at least two bases b > 1.

We shall call a positive integer with this property a strong repunit.
It can be verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}.
Furthermore, the sum of all strong repunits below 1000 equals 15864.
Find the sum of all strong repunits below 10**12.
"""

limit = 10**12
numbers = {1}
# no need to use bases over 1 000 000
for b in range(2, 1000000):
    n = b * b * b
    t = b * b + b + 1
    while t < limit:
        numbers.add(t)
        t += n
        n *= b
print(sum(numbers))
exit()

# too slow :(
total = 1
for i in range(3, 100000):
    for b in range(2, i - 1):
        t = 0
        n = 1
        while t < i:
            t += n
            n *= b
        if t == i:
            print(t, b)
            total += i
            break

print("---")
print(total)
