from AoC.utils import get_input


def move(current_map):
    from copy import deepcopy

    after_horizontal = deepcopy(current_map)
    for y, row in enumerate(current_map):
        for x, cucumber in enumerate(row):
            if cucumber == ">" and row[(x + 1) % len(row)] == ".":
                after_horizontal[y][(x + 1) % len(row)] = ">"
                after_horizontal[y][x] = "."
    after_vertical = deepcopy(after_horizontal)
    for y, row in enumerate(after_horizontal):
        for x, cucumber in enumerate(row):
            if cucumber == "v" and after_horizontal[(y + 1) % len(current_map)][x] == ".":
                after_vertical[(y + 1) % len(current_map)][x] = "v"
                after_vertical[y][x] = "."
    return after_vertical


def find_step(cucumbers_map):
    i = 0
    while True:
        i += 1
        after_move = move(cucumbers_map)
        if cucumbers_map == after_move:
            return i
        cucumbers_map = after_move


print(find_step(get_input(25, lambda y: [x for x in y])))
