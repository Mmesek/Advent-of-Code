from AoC.utils import solve
from collections import defaultdict

example = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
""".splitlines()


def parse(puzzle_input: list[str]) -> tuple[dict[int, list[int]], dict[str, set]]:
    grid = defaultdict(list)
    blizzard = defaultdict(set)

    for y, line in enumerate(puzzle_input):
        for x, char in enumerate(line):
            if char == ".":
                grid[y].append(x)

            if char in "<>^v":
                blizzard[char].add((y, x))

    return grid, blizzard


def move_blizzard(blizzard: dict[str, set[int]], x: int, y: int) -> dict[str, set[int]]:
    """Advances the blizzard by one"""
    new_state = defaultdict(set)
    for direction, values in blizzard.items():
        for value in values:
            if direction == ">":
                # x+1, wrap to 0
                value[1] = (value[1] + 1) % len(x)
            elif direction == "<":
                # x - 1 unless it's below 0 then last x
                value[1] = (value[1] - 1) if (value[1] - 1) > 0 else len(x)
            elif direction == "v":
                # y + 1, wrap to 0. End Y is below regular Ys
                value[0] = (value[0] + 1) % (len(y) - 1)
            elif direction == "^":
                # y - 1 unless it's below 0, then last y - 1. Ditto
                value[0] = (value[0] - 1) if (value[0] - 1) > 0 else len(y) - 1
            new_state[direction].add((value[0], value[1]))
    return new_state


MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         Right,   Left,   Down,     Up


def solution(puzzle_input: list[str]) -> int:
    grid, blizzard = parse(puzzle_input)
    y = min(grid.keys())
    x = min(grid[y])
    end_y = max(grid.keys())
    end_x = max(grid[end_y])
    steps = 0
    while x != end_x and y != end_y:
        blizzard = move_blizzard(blizzard, end_x, end_y)
        options = set()

        for move in MOVES:
            option = (y + move[0], x + move[1])
            if option[1] in grid[option[0]]:
                if not any([option not in direction for direction in blizzard]):
                    options.add(option)

        if not options:
            # pray they are in the eye...
            continue

        for option in options:
            pass

        steps += 1

    return steps


solve(24, 1, solution, lambda x: x, example, (0, 0))
