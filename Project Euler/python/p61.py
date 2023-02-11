# encoding: utf-8

# generar números
nums = [
    [i * (i + 1) // 2 for i in range(45, 141)],
    [i**2 for i in range(32, 100)],
    [i * (3 * i - 1) // 2 for i in range(26, 82)],
    [i * (2 * i - 1) for i in range(23, 71)],
    [i * (5 * i - 3) // 2 for i in range(21, 64)],
    [i * (3 * i - 2) for i in range(19, 59)],
]


def puedeSeguir(inicio, siguiente):
    return inicio % 100 == siguiente // 100


import itertools

ordenes = list(itertools.permutations([0, 1, 2, 3, 4, 5]))

# para cada orden posible, tratar de generar una lista
for orden in ordenes:
    for n0 in nums[orden[0]]:
        for n1 in nums[orden[1]]:
            if puedeSeguir(n0, n1):
                for n2 in nums[orden[2]]:
                    if puedeSeguir(n1, n2):
                        for n3 in nums[orden[3]]:
                            if puedeSeguir(n2, n3):
                                for n4 in nums[orden[4]]:
                                    if puedeSeguir(n3, n4):
                                        for n5 in nums[orden[5]]:
                                            if puedeSeguir(n4, n5) and puedeSeguir(
                                                n5, n0
                                            ):
                                                print(orden)
                                                print(n0, n1, n2, n3, n4, n5)
                                                print(
                                                    "--->", n0 + n1 + n2 + n3 + n4 + n5
                                                )
                                                exit()
