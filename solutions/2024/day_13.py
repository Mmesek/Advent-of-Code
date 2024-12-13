from AoC.utils import solve
from AoC.helpers import Coordinate
from dataclasses import dataclass
from itertools import product

example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".splitlines()


@dataclass
class Machine:
    a: Coordinate = None
    b: Coordinate = None
    prize: Coordinate = None


def prepare(puzzle_input, prize_incr: int = 0) -> list[Machine]:
    machine = Machine()
    machines = []
    puzzle_input.append("")
    for line in puzzle_input:
        if not line:
            machines.append(machine)
            machine = Machine()
            continue
        name, xy = line.split(": ")
        match name:
            case "Button A":
                x, y = xy.split(", ")
                machine.a = Coordinate(
                    int(y.split("+", 1)[-1]), int(x.split("+", 1)[-1])
                )
            case "Button B":
                x, y = xy.split(", ")
                machine.b = Coordinate(
                    int(y.split("+", 1)[-1]), int(x.split("+", 1)[-1])
                )
            case "Prize":
                x, y = xy.split(", ")
                machine.prize = Coordinate(
                    int(y.split("=", 1)[-1]) + prize_incr,
                    int(x.split("=", 1)[-1]) + prize_incr,
                )
    return machines


def solution(puzzle_input: list[str], prize_incr: int = 0, max_range: int = 100) -> int:
    machines = prepare(puzzle_input)
    tokens = []
    for machine in machines:
        for a, b in product(range(max_range + 1), range(max_range + 1)):
            x = machine.a.x * a + machine.b.x * b
            y = machine.a.y * a + machine.b.y * b
            if y == machine.prize.y and x == machine.prize.x:
                tokens.append(a * 3 + b)
                break
    return sum(tokens)


solve(13, 1, solution, lambda x: x, example, 480)
# solve(13, 2, solution, lambda x: x, prize_incr=10000000000000, max_range=100000)
