# encoding: UTF-8


def rToNum(x):
    # un char más para validar la posición siguiente en las restas
    x += " "
    total = 0
    i = 0
    while i < len(x):
        if x[i] == "M":
            total += 1000
        elif x[i] == "D":
            total += 500
        elif x[i] == "C":
            if x[i + 1] == "M":
                total += 900
                i += 1
            elif x[i + 1] == "D":
                total += 400
                i += 1
            else:
                total += 100
        elif x[i] == "L":
            total += 50
        elif x[i] == "X":
            if x[i + 1] == "C":
                total += 90
                i += 1
            elif x[i + 1] == "L":
                total += 40
                i += 1
            else:
                total += 10
        elif x[i] == "V":
            total += 5
        elif x[i] == "I":
            if x[i + 1] == "X":
                total += 9
                i += 1
            elif x[i + 1] == "V":
                total += 4
                i += 1
            else:
                total += 1
        i += 1
    return total


# Sabemos que el mayor es 4998
def numToR(x):
    s = ""
    # Unidades
    c = x % 10
    if c == 1:
        s = "I"
    elif c == 2:
        s = "II"
    elif c == 3:
        s = "III"
    elif c == 4:
        s = "IV"
    elif c == 5:
        s = "V"
    elif c == 6:
        s = "VI"
    elif c == 7:
        s = "VII"
    elif c == 8:
        s = "VIII"
    elif c == 9:
        s = "IX"
    # Decenas
    x /= 10
    c = x % 10
    if c == 1:
        s = "X" + s
    elif c == 2:
        s = "XX" + s
    elif c == 3:
        s = "XXX" + s
    elif c == 4:
        s = "XL" + s
    elif c == 5:
        s = "L" + s
    elif c == 6:
        s = "LX" + s
    elif c == 7:
        s = "LXX" + s
    elif c == 8:
        s = "LXXX" + s
    elif c == 9:
        s = "XC" + s
    # Centenas
    x /= 10
    c = x % 10
    if c == 1:
        s = "C" + s
    elif c == 2:
        s = "CC" + s
    elif c == 3:
        s = "CCC" + s
    elif c == 4:
        s = "CD" + s
    elif c == 5:
        s = "D" + s
    elif c == 6:
        s = "DC" + s
    elif c == 7:
        s = "DCC" + s
    elif c == 8:
        s = "DCCC" + s
    elif c == 9:
        s = "CM" + s
    # Miles
    x /= 10
    c = x % 10
    if c == 1:
        s = "M" + s
    elif c == 2:
        s = "MM" + s
    elif c == 3:
        s = "MMM" + s
    elif c == 4:
        s = "MMMM" + s
    return s


f = open("inputs/p89.in", "r")

ahorro = 0
for line in f:
    num = rToNum(line)
    # largo original
    li = len(line.strip())
    # largo final
    lf = len(numToR(num))
    ahorro += li - lf
print(ahorro)
f.close()
