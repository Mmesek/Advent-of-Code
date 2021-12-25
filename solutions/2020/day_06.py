from AoC.utils import get_input

answers = get_input(6)

p1_group = []
total_p1 = []

group_answers = []
total = []
first = True

for answer in answers:
    if answer == '':
        total_p1.append(len(p1_group))
        p1_group = []

        total.append(len(group_answers))
        group_answers = []
        first = True

    elif first:
        for char in answer:
            group_answers.append(char)
            first = False
    else:
        _group_answers = group_answers.copy()
        for char in group_answers:
            if char not in answer:
                _group_answers.remove(char)
        group_answers = _group_answers.copy()

    if answer != '':
        for char in answer:
            if char not in p1_group:
                p1_group.append(char)

if p1_group != []:
    total_p1.append(len(p1_group))

print(sum(total_p1))

if group_answers != []:
    total.append(len(group_answers))

print(sum(total))
