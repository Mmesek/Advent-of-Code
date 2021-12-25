from AoC.utils import get_input

data = get_input(1, lambda x: int(x))


def count_increments(measurements: list[int]) -> int:
    """Count incrementing measurements from previous one"""
    previous_value = None
    increased = 0
    for value in measurements:
        if previous_value:
            if previous_value < value:
                increased += 1
        previous_value = value
    return increased


print(count_increments(data))
print(count_increments([sum([i, data[x - 1], data[x - 2]]) for x, i in enumerate(data[2:], start=2)]))
