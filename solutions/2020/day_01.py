from AoC.utils import get_input

expense_report = get_input(1, lambda i: int(i))

for x, i in enumerate(expense_report):
    for y, j in enumerate(expense_report[x+1:]):
        if i+j==2020:
            print(i, j)
            print("Part 1:", i*j)
        for k in expense_report[y+1:]:
            if i+j+k==2020:
                print(i, j, k)
                print("Part 2:", i*j*k)