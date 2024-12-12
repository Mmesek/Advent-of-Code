from AoC.utils import solve
from AoC.helpers import Grid, Coordinate
from itertools import pairwise

example = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    g = Grid.make_grid(puzzle_input)
    area = []
    perimeter = []
    visited = set()
    for y, line in enumerate(g._grid.values()):
        for x, char in enumerate(line.values()):
            if Coordinate(y, x) in visited:
                continue
            plot: set[Coordinate] = set()
            _perimeter = []
            for dy, dx, coord in g.find_nearest(y, x, char):
                visited.add(coord)
                plot.add(coord)
                neighbors = 0
                for _dy, _dx, one in g.find_nearest(coord.y, coord.x, char):
                    if coord.neighbour(one):
                        neighbors += 1
                _perimeter.append(1 * (4 - neighbors))
            visited.add(Coordinate(y, x))
            area.append(len(plot))
            perimeter.append(sum(_perimeter))
    return sum(a * b for a, b in zip(area, perimeter))


solve(12, 1, solution, lambda x: x, example, 1930)
