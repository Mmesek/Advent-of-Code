from AoC.utils import solve
from collections import defaultdict
import re

example = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""".splitlines()

PATTERN = re.compile("(\D)|(\d+)")


def parse(puzzle_input: list[str]) -> tuple[dict[int, dict[int, int]], list[str]]:
    grid = {i: defaultdict(list) for i in range(len(puzzle_input[:-2]))}
    for y, line in enumerate(puzzle_input):
        if not line:
            break
        for x, char in enumerate(line):
            if char in "#.":
                grid[y][x] = 0 if char == "#" else 1
    instructions = [i for i in PATTERN.split(puzzle_input[-1]) if i]
    return grid, instructions


def solution(puzzle_input: list[str]) -> int:
    grid, instructions = parse(puzzle_input)
    x, y, facing = min(grid[0].keys()), 0, 0

    for instruction in instructions:
        if instruction.isdigit():
            instruction = int(instruction)
            if facing == 0:
                for i in range(instruction):
                    if not grid[y][(x + i) % len(grid[y])]:
                        break
                # if x + i > max(grid[y].keys()):
                #    if grid[y][min(grid[y].keys())]:
                #        x = min(grid[y].keys()) - 1
                x = (x + max(grid[y].keys()) + i) % len(grid[y].keys())
            elif facing == 1:
                for i in range(instruction):
                    if not grid[(y + i) % len(grid)]:
                        break
                # if y + i > max(grid.keys()):
                #    if grid[min(grid.keys())]:
                #        y = min(grid.keys()) - 1
                y = (y + max(grid.keys()) + i) % len(grid.keys())
            elif facing == 2:
                for i in range(instruction):
                    if not grid[y][(x - i) % len(grid[y])]:
                        break
                # if x - i < min(grid[y].keys()):
                #    if grid[y][max(grid[y].keys())]:
                #        x = max(grid[y].keys()) + 1
                x = (x - max(grid[y].keys()) - i) % len(grid[y].keys())
            else:
                for i in range(instruction):
                    if not grid[(y - i) % len(grid)]:
                        break
                # if y - i > min(grid.keys()):
                #    if grid[max(grid.keys())]:
                #        y = max(grid.keys()) + 1
                y = (y - max(grid.keys()) - i) % len(grid.keys())
        elif instruction == "R":
            facing = (facing + 1) % 4
        elif instruction == "L":
            facing = (facing - 1) % 4

        print(instruction, "=", x, y, facing)

    return 1000 * y + 4 * x + facing


solve(22, 1, solution, lambda x: x, example, 6032, strip=False)
