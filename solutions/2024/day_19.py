from AoC.utils import solve

example = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    patterns = sorted(puzzle_input[0].split(", "), key=lambda x: len(x), reverse=True)
    possible = 0
    for line in puzzle_input[2:]:
        index = 0
        _possible = True
        while index < len(line):
            for pattern in patterns:
                if line[index:].startswith(pattern):
                    index += len(pattern)
                    break
            else:
                _possible = False
                break
        if _possible:
            possible += 1
    return possible


solve(19, 1, solution, lambda x: x, example, 6)
