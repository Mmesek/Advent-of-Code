from AoC.utils import solve
from itertools import zip_longest


example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".splitlines()


def compare(a: int | list[int], b: int | list[int]) -> bool:
    if type(a) is int and type(b) is list:
        a = [a]
    elif type(b) is int and type(a) is list:
        b = [b]

    if type(a) is list:
        for i, j in zip_longest(a, b):
            if i is None:
                return True
            elif j is None:
                return False

            if (is_ordered := compare(i, j)) is not None:
                return is_ordered
    elif a > b:
        return False
    elif a < b:
        return True


def solution(puzzle_input: list[str]) -> int:
    puzzle_input = [_ for _ in puzzle_input if _ is not None]
    grouped = [puzzle_input[x : x + 2] for x in range(0, len(puzzle_input), 2)]
    ordered = 0
    for x, (a, b) in enumerate(grouped, start=1):
        if compare(a, b):
            ordered += x
    return ordered


def solution_2(puzzle_input: list[str]) -> int:
    array = [_ for _ in puzzle_input if _ is not None] + [2, 6]

    for i in range(len(array) - 1):
        for a in range(0, len(array) - i - 1):
            if compare(array[a + 1], array[a]):
                array[a], array[a + 1] = array[a + 1], array[a]

    return (array.index(2) + 1) * (array.index(6) + 1)


solve(13, 1, solution, lambda x: eval(x) if x else None, example, 13)
solve(13, 2, solution_2, lambda x: eval(x) if x else None, example, 140)
