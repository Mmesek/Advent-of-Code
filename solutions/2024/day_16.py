from AoC.utils import solve
from AoC.helpers import Grid, Coordinate

example = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".splitlines()


def rotate(direction, pos: Coordinate):
    if direction == 0:
        new_pos = pos.right()
    elif direction == 1:
        new_pos = pos.down()
    elif direction == 2:
        new_pos = pos.left()
    else:
        new_pos = pos.up()
    if new_pos.on_grid == "#":
        return rotate(direction - 1, pos)
    return direction, new_pos


def solution(puzzle_input: list[str]) -> int:
    g = Grid.make_grid(puzzle_input)
    pos = g.find("S")[0]
    end = g.find("E")[0]
    score = 0
    direction = 0
    while True:
        new_direction, pos = rotate(direction, pos)
        if new_direction == -1:
            new_direction = 3
        elif new_direction == 4:
            new_direction == 0
        if new_direction != direction:
            score += 1000
        else:
            score += 1
        direction = new_direction
        if pos == end:
            break
    return score


solve(16, 1, solution, lambda x: x, example, 7036)
