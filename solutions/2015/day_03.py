from AoC.utils import solve


example = """^>v<""".splitlines()


def move(x, y, direction):
    if direction == "^":
        y -= 1
    elif direction == "v":
        y += 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    return x, y


def solution(puzzle_input: list[str]) -> int:
    x, y = 0, 0
    seen = {(x, y)}
    for direction in list(puzzle_input[0]):
        x, y = move(x, y, direction)
        seen.add((x, y))

    return len(seen)


def solution_2(puzzle_input: list[str]) -> int:
    x, y = 0, 0
    rx, ry = 0, 0
    seen = {(x, y)}
    for i, direction in enumerate(list(puzzle_input[0])):
        if i % 2:
            x, y = move(x, y, direction)
            seen.add((x, y))
        else:
            rx, ry = move(rx, ry, direction)
            seen.add((rx, ry))

    return len(seen)


solve(3, 1, solution, lambda x: x, example, 4)
solve(3, 2, solution_2, lambda x: x, example, 3)
