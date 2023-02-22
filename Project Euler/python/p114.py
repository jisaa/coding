"""
A row measuring seven units in length has red blocks with a minimum length of three units placed on it,
such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.
There are exactly seventeen ways of doing this.

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes.
For example, on a row measuring eight units in length you could use red (3), black (1), and red (4).
"""

# can use more than 2 red pieces
memory = {0: 1, 1: 1, 2: 1, 3: 2, 4: 4, 5: 7, 6: 11, 7: 17}


# got this answer from http://oeis.org/A005252
def fib(x):
    a = b = 1
    while x:
        a, b = b, a + b
        x -= 1
    return a


for i in range(51):
    print(i, fib(i + 1) // 2)
