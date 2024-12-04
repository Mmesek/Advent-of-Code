from AoC.utils import solve
from collections import defaultdict

example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()


def count(graph: defaultdict[list], forward: str = "XMAS", backwards: str = "SAMX"):
    total = 0
    for line in [graph[x] for x in sorted(graph)]:
        line = "".join(line)
        total += line.count(forward)
        total += line.count(backwards)
    return total


def solution(puzzle_input: list[str]) -> int:
    fgraph = defaultdict(list)
    bgraph = defaultdict(list)
    cols = defaultdict(list)
    total = 0
    for y, line in enumerate(puzzle_input):
        total += line.count("XMAS")
        total += line.count("SAMX")
        for x, char in enumerate(line):
            cols[x].append(char)
            fgraph[x + y].append(char)
            bgraph[x - y].append(char)
    total += count(fgraph)
    total += count(bgraph)
    total += count(cols)
    return total


def solution_2(puzzle_input: list[str]) -> int:
    search = list("MAS")
    total = 0
    for y, line in enumerate(puzzle_input):
        if not (0 < y < (len(puzzle_input) - 1)):
            continue
        for x, char in enumerate(line):
            if not (0 < x < (len(line) - 1)):
                continue
            a = [puzzle_input[y - 1][x - 1], char, puzzle_input[y + 1][x + 1]]
            if search not in (a, a[::-1]):
                continue
            b = [puzzle_input[y + 1][x - 1], char, puzzle_input[y - 1][x + 1]]
            if search not in (b, b[::-1]):
                continue
            total += 1
    return total


solve(4, 1, solution, lambda x: x, example, 18)
solve(4, 2, solution_2, lambda x: x, example, 9)
