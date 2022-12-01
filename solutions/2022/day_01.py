from AoC.utils import solve


example = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".splitlines()


def solution(puzzle_input: list[int]) -> int:
    """Sums together group of numbers delimitated by 0 and sorts by descending order"""
    counts = []
    _current = 0

    for line in puzzle_input + [0]:
        if not line:
            counts.append(_current)
            _current = 0

        _current += line

    return sorted(counts, reverse=True)


solve(1, 1, lambda x: max(solution(x)), lambda x: int(x) if x else 0, example, 24000)
solve(1, 2, lambda x: sum(solution(x)[:3]), lambda x: int(x) if x else 0, example, 45000)
