from AoC.utils import solve
from collections import defaultdict
from itertools import cycle

example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    area = defaultdict(dict)
    pos = 0, 0
    longest_x = len([puzzle_input][0]) - 1
    longest_y = len(puzzle_input) - 1
    for y, line in enumerate(puzzle_input):
        for x, char in enumerate(line):
            area[y][x] = True if char == "#" else False
            if char == "^":
                pos = y, x
    walk(pos, area, longest_x, longest_y)


def walk(pos, area, longest_x, longest_y):
    DIRECTIONS = cycle(["UP", "RIGHT", "DOWN", "LEFT"])
    direction = next(DIRECTIONS)
    visited = set()
    while True:
        visited.add(pos)
        y, x = pos
        turn = False
        if y < 0 or x < 0 or y > longest_y or x > longest_x:
            break
        if direction == "UP":
            if y - 1 < 0:
                break
            if not area[y - 1][x]:
                pos = y - 1, x
            else:
                turn = True
        elif direction == "RIGHT":
            if x + 1 > longest_x:
                break
            if not area[y][x + 1]:
                pos = y, x + 1
            else:
                turn = True
        elif direction == "DOWN":
            if y + 1 > longest_y:
                break
            if not area[y + 1][x]:
                pos = y + 1, x
            else:
                turn = True
        elif direction == "LEFT":
            if x - 1 < 0:
                break
            if not area[y][x - 1]:
                pos = y, x - 1
            else:
                turn = True
        if turn:
            direction = next(DIRECTIONS)
    return len(visited)


def print(visited, obstacles):
    x, y = [10], [10]
    for v in visited:
        x.append(v[1])
        y.append(v[0])
    visited = sorted(list(visited))
    x = len(obstacles[0])
    y = len(obstacles)
    arr = []
    for i in range(y + 1):
        line: list[str] = ["."] * x
        for _y, _x in visited:
            if _y == i and _x < len(line):
                line[_x] = "X"
        for _x, obstacle in obstacles[i].items():
            if obstacle:
                if _x < len(line):
                    line[_x] = "#"
        arr.append("".join(line) + "\n")
    with open("map.txt", "w", newline="", encoding="utf-8") as file:
        file.writelines(arr)


solve(6, 1, solution, lambda x: x, example, 41)
# solve(6, 2, solution, lambda x: x, example, 6)
