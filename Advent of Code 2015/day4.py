import hashlib


prefix = "iwrupvqb"
i = 1
solved_part_1 = False
while True:
    md5 = hashlib.md5((prefix + str(i)).encode())
    if not solved_part_1 and md5.hexdigest()[:5] == "00000":
        print("Part 1:", i)
        solved_part_1 = True
    if md5.hexdigest()[:6] == "000000":
        print("Part 2:", i)
        break
    i += 1
