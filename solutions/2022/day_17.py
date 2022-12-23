from AoC.utils import solve
from collections import defaultdict

example = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""".splitlines()


class Rock:
    def __init__(self, indices: tuple[tuple[int]]) -> None:
        self.indices = indices
        self.width = max([i[1] for i in self.indices]) + 1

    def with_offset(self, offset, y):
        return [(_y + y, _x + offset) for _y, _x in self.indices]


SHAPES = [
    Rock(((0, 0), (0, 1), (0, 2), (0, 3))),
    Rock(((0, 1), (1, 0), (1, 1), (1, 2), (2, 1))),
    Rock(((2, 2), (1, 2), (0, 0), (0, 1), (0, 2))),
    Rock(((0, 0), (1, 0), (2, 0), (3, 0))),
    Rock(((0, 0), (0, 1), (1, 0), (1, 1))),
]


def draw(matrix: dict[list[int]], y: int = None, offset: int = None, rock: Rock = None, state: str = ""):
    print(state)

    if rock:
        rock = rock.with_offset(offset, y)

    _max = max([k for k, v in matrix.items() if v] or [0])

    for y in sorted(set(list(matrix.keys()) + list(range(_max, _max + 6))), reverse=True):
        if y < 0:
            continue

        row = []
        for x in range(7):
            if rock and (y, x) in rock:
                row.append("@")
            elif x in matrix[y]:
                row.append("#")
            else:
                row.append(".")

        print("".join(row))

    print()

    if not rock:
        print()


def solution(puzzle_input: list[str], iterations: int = 2022) -> int:
    highest, movement, extra = 0, 0, 0
    moves = puzzle_input[0]
    length = len(moves)
    matrix = defaultdict(list)
    cache = {}
    i = 0
    while i < iterations:
        offset, y = 2, highest + 4
        rock = SHAPES[i % 5]
        should_break = False

        while not should_break:
            if moves[movement % length] == "<":
                if not any(_x - 1 in matrix[_y] for _y, _x in rock.with_offset(offset, y)) and offset - 1 >= 0:
                    offset -= 1
            elif not any(_x + 1 in matrix[_y] for _y, _x in rock.with_offset(offset, y)) and offset + rock.width < 7:
                offset += 1

            movement += 1

            if not (any(_x in matrix[_y - 1] for _y, _x in rock.with_offset(offset, y)) or y - 1 <= 0):
                y -= 1
            else:
                should_break = True

        for _y, _x in rock.with_offset(offset, y):
            matrix[_y].append(_x)

        highest = max([k for k, v in matrix.items() if v])

        value = i % 5, movement % length, tuple(tuple(matrix[y]) for y in range(highest, highest - 31, -1))
        if value in cache.keys():
            iteration, height = cache[value]

            diff = i - iteration
            repeat = (iterations - i) // diff

            extra += (highest - height) * repeat
            i += diff * repeat

        cache[value] = i, highest
        i += 1

    return highest + extra


solve(17, 1, solution, lambda x: x, example, 3068)
solve(17, 2, solution, lambda x: x, example, 1514285714288, iterations=1000000000000)
