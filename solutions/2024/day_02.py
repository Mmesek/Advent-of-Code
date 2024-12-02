from AoC.utils import solve


example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()


def solution(puzzle_input: list[list[int]], skip: bool = False) -> int:
    safe_count = 0
    for report in puzzle_input:
        previous = None
        decreasing = None
        safe = True
        skipped = False
        for level in report:
            if previous:
                if previous < level:
                    if decreasing or abs(level - previous) > 3:
                        if skip and not skipped:
                            skipped = True
                            continue
                        safe = False

                    if decreasing is None:
                        decreasing = False
                elif previous > level:
                    if (
                        not decreasing
                        and decreasing is not None
                        or abs(level - previous) > 3
                    ):
                        if skip and not skipped:
                            skipped = True
                            continue
                        safe = False

                    if decreasing is None:
                        decreasing = True
                elif previous == level:
                    if skip and not skipped:
                        skipped = True
                        continue
                    safe = False
            previous = level
        safe_count += safe
    return safe_count


solve(2, 1, solution, lambda x: [int(i) for i in x.split(" ")], example, 2)
solve(2, 2, solution, lambda x: [int(i) for i in x.split(" ")], example, 4, skip=True)
