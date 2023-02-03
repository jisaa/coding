def step(x, subject_number):
    return (x * subject_number) % 20201227


def findLoopSize(x):
    t = 7
    n = 1
    while t != x:
        t = step(t, 7)
        n += 1
    return n


def transform(subject_number, loop_size):
    x = 1
    for _ in range(loop_size):
        x = step(x, subject_number)
    return x


a = 12578151
b = 5051300

la = findLoopSize(a)
lb = findLoopSize(b)

print(transform(a, lb))
print(transform(b, la))
