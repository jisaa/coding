def get_code(row, col):
    r = c = 1
    code = 20151125
    while r != row or c != col:
        if r == 1:
            r = c + 1
            c = 1
        else:
            r -= 1
            c += 1
        code = (code * 252533) % 33554393
    return code


print("Part 1:", get_code(2947, 3029))
