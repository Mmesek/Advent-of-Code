from AoC.utils import solve
import re

example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

example_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
pattern = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")


def solution(puzzle_input: list[str], pattern: re.Pattern) -> int:
    values = []
    for line in puzzle_input:
        digits = pattern.findall(line)

        if not digits[0].isdigit():
            first = str(DIGITS.index(digits[0]) + 1)
        else:
            first = digits[0]

        if not digits[-1].isdigit():
            last = str(DIGITS.index(digits[-1]) + 1)
        else:
            last = digits[-1]

        values.append(int(str(first + last)))
    return sum(values)


solve(1, 1, lambda x: solution(x, re.compile(r"\d")), lambda x: x, example, 142)
solve(1, 2, lambda x: solution(x, pattern), lambda x: x, example_2, 281)
