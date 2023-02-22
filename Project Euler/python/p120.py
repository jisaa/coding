# encoding: UTF-8

# guardar lista de módulos
# terminar de calcular cuando la lista sea cíclica
suma = 0
for a in range(3, 1001):
    n = 1
    r = []
    m = a**2
    while len(r) < 3 or r[: len(r) // 2] != r[len(r) // 2 :]:
        r.append((pow(a - 1, n, m) + pow(a - 1, n, m)) % m)
        n += 1
    suma += max(r)

print("--->", suma)

"""
Let r be the remainder when (a-1)^n + (a+1)^n is divided by a².

For example, if a = 7 and n = 3, then r = 42: 6³ + 8³ = 728  42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that r_max = 42.

For 3 <= a <= 1000, find sum(r_max).
"""
