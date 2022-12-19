from AoC.utils import solve

example = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".splitlines()


def solution(puzzle_input: list[tuple[int]]) -> int:
    puzzle_input, sides = set(puzzle_input), 0
    for x, y, z in puzzle_input:
        sides += [
            (x - 1, y, z) in puzzle_input,
            (x, y - 1, z) in puzzle_input,
            (x, y, z - 1) in puzzle_input,
            (x + 1, y, z) in puzzle_input,
            (x, y + 1, z) in puzzle_input,
            (x, y, z + 1) in puzzle_input,
        ].count(True)

    return len(puzzle_input) * 6 - sides


def get_neighbours(x: int, y: int, z: int) -> list[tuple[int]]:
    return [
        (x - 1, y, z),
        (x, y - 1, z),
        (x, y, z - 1),
        (x + 1, y, z),
        (x, y + 1, z),
        (x, y, z + 1),
    ]


def solution_2(puzzle_input: list[tuple[int]]) -> int:
    puzzle_input, remaining = set(puzzle_input), [(-1, -1, -1)]
    sides, seen = 0, set()

    while remaining:
        for neighbour in get_neighbours(*remaining.pop()):
            if all([-1 <= i <= 25 for i in neighbour]):
                if neighbour in puzzle_input:
                    sides += 1
                else:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        remaining.append(neighbour)

    return sides


solve(18, 1, solution, lambda x: tuple([int(i) for i in x.split(",")]), example, 64)
solve(18, 2, solution_2, lambda x: tuple([int(i) for i in x.split(",")]), example, 58)
