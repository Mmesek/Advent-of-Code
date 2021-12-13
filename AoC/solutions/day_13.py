from typing import DefaultDict
from AoC.utils import get_input


def prepare(arr: list[str]) -> tuple[list[list[int], tuple[str, int]]]:
    """Retrives Coordinates and Folding instructions from input"""
    coords = []
    folding = []
    instructions = False
    for x, line in enumerate(arr):
        if line == "":
            instructions = True
            continue
        if instructions:
            x, pos = line.split(" ")[-1].split("=")
            folding.append((x, int(pos)))
        else:
            coords.append([int(i) for i in line.split(",")])
    return coords, folding


def draw(coords: list[tuple[int, int]]) -> None:
    """Prints coordinates onto terminal on xy matrix"""
    mapped = DefaultDict(lambda: [])
    top_x = 0

    for x, y in coords:
        if x > top_x:
            top_x = x
        mapped[y].append(x)
    top_x += 1

    last_y = 0
    highest_y = max(list(mapped.keys()))
    for y in range(highest_y + 1):
        line = "." * top_x
        line = list(line)
        for x in mapped[y]:
            line[x] = "#"
        for missed in range(last_y, y - 1):
            print("." * top_x)
        last_y = y
        print(" ".join(line))


def fold(fold_at: int, by_axis: str, coords: list[list[int]]) -> list[list[int]]:
    """Folds coordinates according to axis"""
    for pos, (x, y) in enumerate(coords):
        if by_axis == "x" and x >= fold_at:
            coords[pos][0] = fold_at - (x - fold_at)
        elif by_axis == "y" and y >= fold_at:
            coords[pos][1] = fold_at - (y - fold_at)
    return coords


def follow_instructions(coords: list[list[int]], folding: list[tuple[str, int]]):
    """Follows folding instructions and prints dots"""
    for x, (axis, fold_at) in enumerate(folding):
        coords = fold(fold_at, axis, coords)
        c = sorted(list(set([tuple(i) for i in coords])), key=lambda x: (x[1], x[0]))
        if x == 0:
            print(len(set(c)))
    draw(c)


coords, folding = prepare(get_input(13))
follow_instructions(coords, folding)
