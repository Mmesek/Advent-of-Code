from AoC.utils import solve
from AoC.helpers import Grid, Coordinate

example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()


def check_antinode(coordinate: Coordinate, mirror: Coordinate, g: Grid, antinodes: set):
    if coordinate != mirror and coordinate.within_bounds(g.height, g.length):
        antinodes.add(coordinate)


def distance(
    coordinate: Coordinate,
    func,
    mirror: Coordinate,
    g: Grid,
    antinodes: set,
    single_pass: bool = True,
):
    while coordinate.within_bounds(g.height, g.length):
        coordinate: Coordinate = func(coordinate)
        check_antinode(coordinate, mirror, g, antinodes)
        if single_pass:
            break


def check(char: str, g: Grid, antinodes: set, part2: bool = True):
    for f in g.find(char):
        for dy, dx, c in g.find_nearest(f.y, f.x, char):
            if c == f:
                continue
            if not part2:
                antinodes.add(c)
                antinodes.add(f)
            distance(f, lambda x: x + (dy, dx), c, g, antinodes, part2)
            distance(f, lambda x: x - (dy, dx), c, g, antinodes, part2)


def solution(puzzle_input: list[str], part2: bool = True) -> int:
    g = Grid.make_grid(puzzle_input)
    antinodes = set()
    for char in g.grid_characters:
        if char != ".":
            check(char, g, antinodes, part2)

    return len(antinodes)


solve(8, 1, solution, lambda x: x, example, 14)
solve(8, 2, solution, lambda x: x, example, 34, part2=False)
