from AoC.utils import get_input

data = get_input(1, lambda x: int(x))

def change(measurements: list[int]) -> int:
    previous_value = None
    increased = 0
    for value in measurements:
        if not previous_value:
            previous_value = value
        else:
            if previous_value < value:
                increased += 1
            previous_value = value
    return increased

print(change(data))
print(change([sum([i, data[x-1], data[x-2]]) for x, i in enumerate(data[2:], start=2)]))
