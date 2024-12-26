from AoC.utils import solve
from itertools import product

example = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    locks = []
    keys = []
    is_lock = False
    columns = [-1] * 5
    new = True
    row = 0
    for line in puzzle_input + [""]:
        if not line:
            if is_lock:
                locks.append(columns)
            else:
                keys.append(columns)
            columns = [-1] * 5
            row = 0
            continue

        if new and "#" * 5 == line:
            is_lock = False
        elif new:
            is_lock = True

        for x, char in enumerate(line):
            if char == "#":
                columns[x] += 1
        row += 1

    paired_keys = []

    pairs = 0
    for lock, key in product(locks, keys):
        if key in paired_keys:
            continue

        overlap = False
        highest_k = max(key)
        highest_l = max(lock)

        for a, b in zip(lock, key):
            if not a or not b:
                continue

            row = highest_k - b
            column = highest_l - a

            if row > column:
                overlap = True
                break

        if not overlap:
            pairs += 1
            paired_keys.append((lock, key))

    return pairs


solve(25, 1, solution, lambda x: x, example, 3)
