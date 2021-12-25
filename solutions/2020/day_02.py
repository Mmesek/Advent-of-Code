from AoC.utils import get_input

passwords = get_input(2)

valid = 0
valid2 = 0

for password in passwords:
    p = password.split(':')
    password = p[1]
    p = p[0].split(' ')
    letter = p[1]
    _min = int(p[0].split('-')[0])
    _max = int(p[0].split('-')[1])

    if password.count(letter) >= _min and password.count(letter) <= _max:
        valid += 1

    if (letter == password[_min] and letter != password[_max]) or (letter != password[_min] and letter == password[_max]):
        valid2 += 1

print(valid)
print(valid2)
