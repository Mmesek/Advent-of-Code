from AoC.utils import solve


example = """2x3x4
1x1x10""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    total, ribbon = 0, 0
    for present in puzzle_input:
        l, w, h = [int(i) for i in present.split("x")]
        a, b, c = l * w, w * h, h * l
        total += 2 * a + 2 * b + 2 * c + min((a, b, c))
        a, b, c = sorted((l, w, h))
        ribbon += a + a + b + b + a * b * c

    return total, ribbon


solve(2, 1, solution, lambda x: x, example, (101, 48))
