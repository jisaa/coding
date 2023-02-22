"""
The binomial coefficients nCk can be arranged in triangular form, Pascal's triangle, like this:
1
1		1
1		2		1
1		3		3		1
1		4		6		4		1
1		5		10		10		5		1
1		6		15		20		15		6		1
1		7		21		35		35		21		7		1
.........

It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers:
 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n.
Of the twelve distinct numbers in the first eight rows of Pascal's triangle, all except 4 and 20 are squarefree.
The sum of the distinct squarefree numbers in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.

"""

p = [[1]]
while len(p) < 51:
    n = [1]
    for i in range(1, len(p[-1])):
        n.append(p[-1][i] + p[-1][i - 1])
    n.append(1)
    p.append(n)

numbers = set()
for r in p:
    for i in r:
        numbers.add(i)

limit = max(p[-1]) ** 0.5

prime_squares = []
with open("primes.txt") as f:
    for line in f:
        p = int(line)
        ps = p * p
        if ps > limit:
            break
        prime_squares.append(ps)


total = 0
for n in numbers:
    squarefree = True
    for d in prime_squares:
        if n % d == 0:
            squarefree = False
            break
    if squarefree:
        total += n

print(total)
