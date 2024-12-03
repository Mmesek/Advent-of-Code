import re
from AoC.utils import solve


example = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))""".splitlines()
example_2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))""".splitlines()
PATTERN = re.compile(r"mul\((\d+),(\d+)\)")
PATTERN_2 = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")


def solution(puzzle_input: list[str]) -> int:
    result = 0
    for line in puzzle_input:
        for group in PATTERN.findall(line):
            result += int(group[0]) * int(group[1])
    return result


def solution_2(puzzle_input: list[str]) -> int:
    result = 0
    on = True
    for line in puzzle_input:
        for a, b, do, dont in PATTERN_2.findall(line):
            if dont:
                on = False
            elif do:
                on = True
            elif on:
                result += int(a) * int(b)
    return result


solve(3, 1, solution, lambda x: x, example, 161)
solve(3, 2, solution_2, lambda x: x, example_2, 48)
