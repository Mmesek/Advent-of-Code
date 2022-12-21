from AoC.utils import solve


example = """1
2
-3
3
-2
0
4
""".splitlines()


def solution(puzzle_input: list[int], mix: int = 1, multiply_by: int = 1) -> int:
    puzzle_input = [i * multiply_by for i in puzzle_input]

    mixed = puzzle_input.copy()
    indices = list(range(len(puzzle_input)))
    for _ in range(mix):
        for x, number in enumerate(puzzle_input):
            index = indices.index(x)
            item = indices.pop(index)
            indices.insert((index + number) % len(indices), item)

    mixed = [puzzle_input[x] for x in indices]

    zero = mixed.index(0)
    length = len(mixed)

    return mixed[(zero + 1000) % length] + mixed[(zero + 2000) % length] + mixed[(zero + 3000) % length]


solve(20, 1, solution, int, example, 3)
solve(20, 2, solution, int, example, 1623178306, mix=10, multiply_by=811589153)
