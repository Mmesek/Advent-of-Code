from AoC.utils import solve

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()


def check_bounding(matrix: list[list[str]], y: int, x: int) -> bool:
    if x - 1 >= 0 and not matrix[y][x - 1].isdigit() and matrix[y][x - 1] != ".":
        return True
    if x + 1 <= len(matrix[y]) - 1 and not matrix[y][x + 1].isdigit() and matrix[y][x + 1] != ".":
        return True
    if y + 1 <= len(matrix) - 1 and x - 1 >= 0 and not matrix[y + 1][x - 1].isdigit() and matrix[y + 1][x - 1] != ".":
        return True
    if y + 1 <= len(matrix) - 1 and not matrix[y + 1][x].isdigit() and matrix[y + 1][x] != ".":
        return True
    if (
        y + 1 <= len(matrix) - 1
        and x + 1 <= len(matrix[y + 1]) - 1
        and not matrix[y + 1][x + 1].isdigit()
        and matrix[y + 1][x + 1] != "."
    ):
        return True
    if y - 1 >= 0 and x - 1 >= 0 and not matrix[y - 1][x - 1].isdigit() and matrix[y - 1][x - 1] != ".":
        return True
    if y - 1 >= 0 and not matrix[y - 1][x].isdigit() and matrix[y - 1][x] != ".":
        return True
    if (
        y - 1 >= 0
        and x + 1 <= len(matrix[y - 1]) - 1
        and not matrix[y - 1][x + 1].isdigit()
        and matrix[y - 1][x + 1] != "."
    ):
        return True
    return False


def solution(puzzle_input: list[str]) -> int:
    numbers = []
    for y, line in enumerate(puzzle_input):
        bbox = False
        number = ""
        for x, char in enumerate(line):
            if char.isdigit():
                number += char
                if check_bounding(puzzle_input, y, x):
                    bbox = True
            if (not char.isdigit() or x == len(line) - 1) and number and bbox:
                bbox = False
                numbers.append(number)
                number = ""
            elif not char.isdigit():
                number = ""
    return sum([int(i) for i in numbers])


solve(3, 1, solution, lambda x: x, example, 4361)
