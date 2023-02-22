required = "byr iyr eyr hgt hcl ecl pid".split()

valid = 0
found = [0] * len(required)
for line in open("inputs/day4.in"):
    line = line.strip()
    if line:
        for pair in line.split(" "):
            field, value = pair.split(":")
            if field in required:
                found[required.index(field)] = 1
            if field == "byr" and not (1920 <= int(value) <= 2002):
                found.append(0)
            if field == "iyr" and not (2010 <= int(value) <= 2020):
                found.append(0)
            if field == "eyr" and not (2020 <= int(value) <= 2030):
                found.append(0)
            if field == "hgt":
                if value[-2:] not in ["cm", "in"]:
                    found.append(0)
                if value[-1] == "m" and not (150 <= int(value[:-2]) <= 193):
                    found.append(0)
                if value[-1] == "n" and not (59 <= int(value[:-2]) <= 76):
                    found.append(0)
            if field == "hcl" and not (
                value[0] == "#" and all(c in "1234567890abcdef" for c in value[1:])
            ):
                found.append(0)
            if field == "ecl" and not (value in "amb blu brn gry grn hzl oth".split()):
                found.append(0)
            if field == "pid" and not (
                len(value) == 9 and all(c in "1234567890" for c in value)
            ):
                found.append(0)

    else:
        valid += all(found)
        found = [0] * len(required)

print(valid)
