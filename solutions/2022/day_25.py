from AoC.utils import solve


example = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
""".splitlines()

SNAFU = {"0": 0, "1": 1, "2": 2, "=": -2, "-": -1}
KEYS = list(SNAFU.keys())


def solution(puzzle_input: list[str]) -> int:
    numbers, snafu = [], []

    for line in puzzle_input:
        number = []

        for power, char in enumerate(line[::-1]):
            number.append(SNAFU[char] * (5**power))

        numbers.append(sum(number))

    final = sum(numbers)

    while final:
        snafu.append(KEYS[final % 5])

        if KEYS[final % 5] in "=-":
            final += ((final % 5) % 2) + 1

        final //= 5

    return "".join(snafu[::-1])


solve(25, 1, solution, lambda x: x, example, "2=-1=0")
