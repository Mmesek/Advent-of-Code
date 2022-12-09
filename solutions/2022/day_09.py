from AoC.utils import solve

example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".splitlines()


def solution(puzzle_input: list[str], total_knots: int = 2) -> int:
    knots = [[0, 0] for _ in range(total_knots)]
    seen = set()

    for direction, steps in puzzle_input:
        for _ in range(steps):
            if direction == "R":
                knots[0][0] += 1
            elif direction == "L":
                knots[0][0] -= 1
            elif direction == "U":
                knots[0][1] += 1
            elif direction == "D":
                knots[0][1] -= 1

            for x, knot in enumerate(knots[1:]):
                head = knots[x]
                if abs(knot[0] - head[0]) > 1 or abs(knot[1] - head[1]) > 1:
                    if head[0] > knot[0]:
                        knot[0] += 1
                    if head[0] < knot[0]:
                        knot[0] -= 1
                    if head[1] < knot[1]:
                        knot[1] -= 1
                    if head[1] > knot[1]:
                        knot[1] += 1

            seen.add(tuple(knots[-1]))

    return len(seen)


solve(9, 1, solution, lambda x: [x.split()[0], int(x.split()[-1])], example, 13)
solve(9, 2, solution, lambda x: [x.split()[0], int(x.split()[-1])], example, 1, total_knots=10)
