passports = 0
field_req = {
    "byr": (4, (1920, 2002)),
    "iyr": (4, (2010, 2020)),
    "eyr": (4, (2020, 2030)),
}
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
last_present = []
invalid = []
from AoC.utils import get_input
lines = get_input(4)
for line in lines:
    if line == "":
        if invalid != []:
            breakpoint
        if all(i in last_present for i in fields):
            passports += 1
        last_present = []
        invalid = []
    else:
        values = line.split(' ')
        for value in values:
            field = value.split(':')
            key = field[0]
            value = field[1].strip()
            valid = False
            try:
                if key in field_req:
                    r = field_req.get(key)
                    if len(value) == r[0]:
                        if int(value) >= r[1][0] and int(value) <= r[1][1]:
                            valid = True
                elif key == 'ecl':
                    if value in ["amb", "blu","brn", "gry", "grn", "hzl", "oth"]:
                        valid = True
                elif key == 'hcl' and value[0] == '#' and len(value)==7:
                    if all(i.lower() in '0123456789abcdef' for i in value[1:]):
                      valid = True
                elif key == 'pid':
                    if len(value) == 9:
                        if all(i in '0123456789' for i in value):
                            valid = True
                elif key == 'hgt':
                    if value[-2:] == 'cm':
                        if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                            valid = True
                    elif value[-2:] == 'in':
                        if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                            valid = True
                elif key == 'cid':
                    valid = True
            except Exception as ex:
                print(ex)
                valid = False
            if valid:
                last_present.append(field[0])
            else:
                invalid.append((field[0], field[1].strip()))

#Required here despite not needed in part 1?
if last_present != []:
    if all(i in last_present for i in fields):
        passports += 1

print(passports)
