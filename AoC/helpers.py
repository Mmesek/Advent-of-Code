from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Coordinate:
    y: int
    x: int

    def within_bounds(self, height: int, length: int):
        r = 0 <= self.y <= height and 0 <= self.x <= length
        return r

    def __add__(self, other: tuple[int, int]):
        return Coordinate(self.y + other[0], self.x + other[1])

    def __sub__(self, other: tuple[int, int]):
        return Coordinate(self.y - other[0], self.x - other[1])

    def __eq__(self, value: "Coordinate"):
        return self.x == value.x and self.y == value.y

    def __hash__(self):
        return hash((self.y, self.x))


class Grid:
    def __init__(self, grid: dict[int, dict[int, str]]):
        self._grid = grid
        self.length = max([len(i) for i in grid.values()]) - 1
        self.height = len(grid) - 1
        self.grid_characters = set(
            i for line in self._grid.values() for i in line.values()
        )

    @classmethod
    def make_grid(cls, puzzle_input: list[str]):
        grid = defaultdict(dict)
        for y, line in enumerate(puzzle_input):
            for x, char in enumerate(line):
                grid[y][x] = char
        _grid = {}
        for k, v in grid.items():
            _grid[k] = v
        return cls(_grid)

    def find(self, char: str) -> list[Coordinate]:
        coords = []
        for y, line in self.grid.items():
            for x, _char in line.items():
                if char == _char:
                    coords.append(Coordinate(y, x))
        return coords

    def find_nearest(
        self, y: int, x: int, char: str
    ) -> list[tuple[int, int, Coordinate]]:
        distances = []
        coords = self.find(char)
        for coord in coords:
            a = coord.y - y
            b = coord.x - x
            distances.append((a, b, coord))
        return sorted(distances, key=lambda x: (abs(x[0]), abs(x[1])))

    def __getitem__(self, index: tuple[int, int]) -> str:
        return self._grid[index[0]][index[1]]

    @property
    def grid(self):
        return self._grid

    def _print(self):
        arr = []
        for y in self.grid.values():
            arr.append("".join(y.values()) + "\n")
        return arr

    def print(self):
        arr = self._print()
        print("".join(arr))

    def print_to_file(self):
        arr = self._print()
        with open("map.txt", "w", newline="", encoding="utf-8") as file:
            file.writelines(arr)
