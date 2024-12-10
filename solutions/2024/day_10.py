from AoC.utils import solve
from AoC.helpers import Grid, Coordinate

example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()


def check(coord: Coordinate, expected_value: int):
    if coord.within_bounds() and coord.on_grid == expected_value:
        return True
    return False


def get_trailheads(coord: Coordinate, next_step: int = 0):
    visited = set()
    next_step += 1
    if next_step == 10:
        return {coord}
    if check(coord.up(), next_step):
        visited.update(get_trailheads(coord.up(), next_step))
    if check(coord.down(), next_step):
        visited.update(get_trailheads(coord.down(), next_step))
    if check(coord.left(), next_step):
        visited.update(get_trailheads(coord.left(), next_step))
    if check(coord.right(), next_step):
        visited.update(get_trailheads(coord.right(), next_step))

    return visited


def get_ratings(coord: Coordinate, next_step: int = 0):
    rating = 0

    next_step += 1
    if next_step == 10:
        return rating + 1
    if check(coord.up(), next_step):
        if r := get_ratings(coord.up(), next_step):
            rating += r

    if check(coord.down(), next_step):
        if r := get_ratings(coord.down(), next_step):
            rating += r

    if check(coord.left(), next_step):
        if r := get_ratings(coord.left(), next_step):
            rating += r

    if check(coord.right(), next_step):
        if r := get_ratings(coord.right(), next_step):
            rating += r

    return rating


def solution(puzzle_input: list[str]) -> int:
    g = Grid.make_grid(puzzle_input)
    trailheads = []
    for x, start in enumerate(g.find(0)):
        if end := get_trailheads(start):
            trailheads.append(len(end))
    return sum(trailheads)


def solution_2(puzzle_input: list[str]) -> int:
    g = Grid.make_grid(puzzle_input)
    trailheads = []
    for x, start in enumerate(g.find(0)):
        if end := get_ratings(start):
            trailheads.append(end)
    return sum(trailheads)


solve(10, 1, solution, lambda x: [int(i) for i in x], example, 36)
solve(10, 2, solution_2, lambda x: [int(i) for i in x], example, 81)
