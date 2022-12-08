from AoC.utils import solve

example = """30373
25512
65332
33549
35390
""".splitlines()


def view_distance(tree_line: list[int], tree: int) -> int:
    v = 0
    for _tree in tree_line:
        v += 1
        if _tree >= tree:
            break
    return v


def solution(puzzle_input: list[str]) -> int:
    visible = 0
    for y, row in enumerate(puzzle_input[1:-1], start=1):
        for x, tree in enumerate(row[1:-1], start=1):
            if (
                all([puzzle_input[i][x] < tree for i in range(0, y)])
                or all([puzzle_input[i][x] < tree for i in range(y + 1, len(puzzle_input))])
                or all([puzzle_input[y][i] < tree for i in range(0, x)])
                or all([puzzle_input[y][i] < tree for i in range(x + 1, len(puzzle_input[y]))])
            ):
                visible += 1

    return visible + len(puzzle_input) * 2 + (len(row) - 2) * 2


def solution_2(puzzle_input: list[str]) -> int:
    score = 0
    for y, row in enumerate(puzzle_input[1:-1], start=1):
        for x, tree in enumerate(row[1:-1], start=1):
            _score = (
                view_distance([puzzle_input[i][x] for i in range(y - 1, -1, -1)], tree)
                * view_distance([puzzle_input[y][i] for i in range(x - 1, -1, -1)], tree)
                * view_distance([puzzle_input[i][x] for i in range(y + 1, len(puzzle_input[y]))], tree)
                * view_distance([puzzle_input[y][i] for i in range(x + 1, len(puzzle_input[y]))], tree)
            )
            if _score > score:
                score = _score

    return score


solve(8, 1, solution, lambda x: [int(i) for i in x], example, 21)
solve(8, 2, solution_2, lambda x: [int(i) for i in x], example, 8)
