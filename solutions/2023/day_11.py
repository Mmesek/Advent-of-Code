from AoC.utils import solve
from itertools import combinations


example = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()


def solution(puzzle_input: list[str], expand: int = 1) -> int:
    galaxies = []

    expanded_y = 0
    for line in puzzle_input:
        expanded_x = 0
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((expanded_x, expanded_y))

            expanded_x += 1
            if all(_line[x] == "." for _line in puzzle_input):
                expanded_x += expand

        expanded_y += 1
        if set(line) == {"."}:
            expanded_y += expand

    distances = []

    for a, b in combinations(galaxies, 2):
        distances.append(abs(a[0] - b[0]) + abs(a[1] - b[1]))

    return sum(distances)


solve(11, 1, solution, lambda x: x, example, 374)
solve(11, 2, lambda x: solution(x, 1000000 - 1), lambda x: x, example, None)
