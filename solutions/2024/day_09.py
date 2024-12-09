from AoC.utils import solve
from copy import copy

example = """2333133121414131402""".splitlines()


def checksum(fs: list[int]):
    result = 0
    for position, file in enumerate(fs):
        if file == ".":
            continue
        result += position * file
    return result


def prepare(
    puzzle_input: list[str], append: bool = False
) -> list[int | str] | list[list[int | str]]:
    files = []
    file_id = 0
    for x, char in enumerate(puzzle_input[0]):
        if x % 2:
            if append:
                files.append(["."] * int(char))
            else:
                files.extend(["."] * int(char))
        else:
            if append:
                files.append([int(file_id)] * int(char))
            else:
                files.extend([int(file_id)] * int(char))
            file_id += 1
    return files


def solution(puzzle_input: list[str]) -> int:
    files = prepare(puzzle_input)

    while "." in files:
        while files[-1] == ".":
            files.pop()
        files[files.index(".")] = files.pop()

    return checksum(files)


def solution_2(puzzle_input: list[str]) -> int:
    files = prepare(puzzle_input, True)

    for y, block in enumerate(files[::-1], 1):
        if set(files[-1]) == "." or files[-1] == []:
            files.pop()
            continue
        for z, next_free_block in enumerate(files):
            if set(next_free_block) != {"."}:
                continue
            if z > (len(files) - y):
                break
            if len(block) <= len(next_free_block):
                if set(block) == {"."} or not block:
                    continue
                for x, (old, new) in enumerate(zip(next_free_block, block)):
                    files[z][x] = new
                    block[x] = old
                if "." in files[z]:
                    leftover = files[z][x + 1 :]
                    files[z] = files[z][: x + 1]
                    files.insert(z + 1, leftover)
    unnested = []
    for i in files:
        unnested.extend(i)

    return checksum(unnested)


solve(9, 1, solution, lambda x: x, example, 1928)
solve(9, 2, solution_2, lambda x: x, example, 2858)
