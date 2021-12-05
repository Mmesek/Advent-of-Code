from AoC.utils import get_input

lines = get_input(
    5, lambda i: [[int(coord) for coord in coords.strip().split(",") if coord] for coords in i.split(" -> ") if coords]
)

from collections import Counter


def plot(xy: list[tuple[int, int]]) -> Counter:
    counter = Counter()
    for start, end in xy:
        diagonal = False
        if start[0] != end[0] and start[1] != end[1]:
            diagonal = True
        for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                counter[(x, y)] += 1
                if diagonal:
                    break
    return counter


def count_total(counter: Counter) -> int:
    total = 0
    for i in counter:
        if counter[i] > 1:
            total += 1
    return total


print(count_total(plot(list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lines)))))
print(count_total(plot(lines)))
