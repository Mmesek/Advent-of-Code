from AoC.utils import solve


example = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    CYCLES = {i for i in range(20, 221, 40)}
    cycle, x = 1, 1
    total = 0

    for instr in puzzle_input:
        if instr == "noop":
            cycle += 1
        else:
            cycle += 1
            if cycle in CYCLES:
                total += cycle * x
            x += int(instr.split()[-1])
            cycle += 1

        if cycle in CYCLES:
            total += cycle * x

        if cycle > max(CYCLES):
            break

    return total


def solution_2(puzzle_input: list[str]) -> str:
    cycle, x = 1, 1

    screen = [["." for _ in range(40)] for _ in range(6)]

    for instr in puzzle_input:
        draw_at = list(range(x, x + 3))

        if instr == "noop":
            screen[(cycle - 1) // 40][cycle % 40 - 1] = "#" if cycle % 40 in draw_at else "."
            cycle += 1
        else:
            screen[(cycle - 1) // 40][cycle % 40 - 1] = "#" if cycle % 40 in draw_at else "."
            cycle += 1

            x += int(instr.split()[-1])

            screen[(cycle - 1) // 40][cycle % 40 - 1] = "#" if cycle % 40 in draw_at else "."
            cycle += 1

    return "\n".join(["".join(line) for line in screen])


example_result = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......###.
#######.......#######.......#######....."""

solve(10, 1, solution, lambda x: x, example, 13140)
solve(10, 2, solution_2, lambda x: x, example, example_result)
