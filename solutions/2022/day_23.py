from AoC.utils import solve
from collections import defaultdict

example = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
""".splitlines()


class Elf:
    def __init__(self, x, y, grid) -> None:
        self.x: int = x
        self.y: int = y
        self.candidate = None
        self.grid: dict[int, set[int]] = grid
        self.y_order: list[int] = [-1, 1, 0, 0]  # N, S, W, E
        self.x_order: list[int] = [0, 0, -1, 1]  # N, S, W, E
        self.diagonal: list[tuple[tuple[int]]] = [
            ((0, 1), (0, -1)),  # NE, NW
            ((0, 1), (0, -1)),  # SE, SW
            ((-1, -1), (1, -1)),  # NW, SW
            ((-1, 1), (1, 1)),  # NE, SE
        ]

    def propose(self, i=0):
        diagonal = self.diagonal.pop(0)
        self.diagonal.append(diagonal)
        y = self.y_order.pop(0)
        self.y_order.append(y)
        x = self.x_order.pop(0)
        self.x_order.append(x)
        if (
            self.x + x not in self.grid[self.y + y]
            and self.x + x + diagonal[0][1] not in self.grid[self.y + y + diagonal[0][0]]
            and self.x + x + diagonal[1][1] not in self.grid[self.y + y + diagonal[1][0]]
        ):
            self.candidate = self.y + y, self.x + x
        elif i < 3:
            self.propose(i + 1)

    def check(self):
        x, y = self.x, self.y
        if any(
            [
                x - 1 in self.grid[y - 1],
                x in self.grid[y - 1],
                x + 1 in self.grid[y - 1],
                x - 1 in self.grid[y],
                x + 1 in self.grid[y],
                x - 1 in self.grid[y + 1],
                x in self.grid[y + 1],
                x + 1 in self.grid[y + 1],
            ]
        ):
            return False
        return True

    def move(self):
        if not self.candidate:
            return

        y, x = self.candidate
        self.grid[self.y].remove(self.x)
        self.grid[y].add(x)
        self.x, self.y = x, y


def solution(puzzle_input: list[str]) -> int:
    grid: dict[int, set[int]] = defaultdict(set)
    elves: list[Elf] = []
    for y, line in enumerate(puzzle_input):
        for x, char in enumerate(line):
            if char == "#":
                elves.append(Elf(x, y, grid))
                grid[y].add(x)

    for _ in range(11):
        for elf in elves:
            if elf.check():
                continue
            elf.propose()

        for elf in elves:
            if elf.check():
                continue

            for second_elf in elves:
                if elf.x == second_elf.x and elf.y == second_elf.y:
                    continue
                if elf.candidate == second_elf.candidate:
                    elf.candidate = None
                    second_elf.candidate = None
            elf.move()

    empty = 0
    x_max, x_min = 0, 0
    y_min, y_max = None, 0
    for y in sorted(grid):
        if y_min is None and grid[y]:
            y_min = y
        if grid[y]:
            y_max = y
        x_min = min(min(grid[y] or [0]), x_min)
        x_max = max(max(grid[y] or [0]), x_max)

    total = ((x_max - x_min) + 1) * ((y_max - y_min) + 1)

    for y in grid:
        if y_max < y or y < y_min:
            continue
        empty += x_max - x_min

    return empty


solve(23, 1, solution, lambda x: x, example, 110)
