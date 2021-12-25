from AoC.utils import get_input
numbers = get_input(15, lambda i: [int(j) for j in i.split(',')])[0]

def calc(initial_numbers, target_round):
    ages = {i: current_round for current_round, i in enumerate(initial_numbers, 1)}
    last_spoken = ages.copy()

    last_number_spoken = initial_numbers[-1]

    for turn in range(len(initial_numbers)+1, target_round+1):
        if last_number_spoken not in last_spoken:
            speak = 0
        else:
            speak = last_spoken[last_number_spoken] - ages[last_number_spoken]
            ages[speak] = last_spoken.get(speak, turn)
        last_spoken[speak] = turn
        last_number_spoken = speak
    return last_number_spoken

print("Part 1:", calc(numbers, 2020))
print("Part 2:", calc(numbers, 30000000))