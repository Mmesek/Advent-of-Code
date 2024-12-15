from AoC.utils import solve
from AoC.helpers import Grid, Coordinate

example = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<""".splitlines()


def parse(puzzle):
    grid = []
    is_grid = True
    moves = []
    for line in puzzle:
        if not line:
            is_grid = False
        if is_grid:
            grid.append(line)
        else:
            moves.append(line)
    moves = "".join(moves)
    g = Grid.make_grid(grid)
    return g, moves


def calculate_gps(box: Coordinate):
    return box.y * 100 + box.x


def change(pos: Coordinate, origin: Coordinate):
    pos.grid._grid[pos.y][pos.x] = origin.on_grid
    origin.grid._grid[origin.y][origin.x] = "."


def move(direction: str, origin: Coordinate):
    if direction == "^":
        pos = origin.up()
    elif direction == ">":
        pos = origin.right()
    elif direction == "<":
        pos = origin.left()
    else:
        pos = origin.down()

    if pos.on_grid == "#":
        return False
    elif pos.on_grid == "O":
        if move(direction, pos):
            change(pos, origin)
    elif pos.on_grid == ".":
        change(pos, origin)
        return pos


def solution(puzzle_input: list[str]) -> int:
    g, moves = parse(puzzle_input)

    robot = g.find("@")[0]
    for direction in moves:
        if new_pos := move(direction, robot):
            robot = new_pos
        print(direction)
        g.print()

    gps = 0
    for box in g.find("O"):
        gps += calculate_gps(box)

    return gps


solve(15, 1, solution, lambda x: x, example, 2028)
