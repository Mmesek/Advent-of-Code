from AoC.utils import solve
from enum import Enum


example = """A Y
B X
C Z
""".splitlines()


class Moves(Enum):
    A = "Rock"
    B = "Paper"
    C = "Scissors"
    X = "Rock"
    Y = "Paper"
    Z = "Scissors"


weight = {
    Moves.A: 1,
    Moves.B: 2,
    Moves.C: 3,
}

wins = {Moves.A: Moves.B, Moves.B: Moves.C, Moves.C: Moves.A}
loses = {v: k for k, v in wins.items()}


def solution(puzzle_input: list[str]) -> int:
    total_points = 0

    for i in puzzle_input:
        a, b = i.split(" ")
        a = Moves.__getitem__(a)
        b = Moves.__getitem__(b)

        if wins.get(a) == b:
            total_points += 6
        elif a == b:
            total_points += 3
        total_points += weight.get(b)

    return total_points


def solution_2(puzzle_input: list[str]) -> int:
    total_points = 0

    for i in puzzle_input:
        a, b = i.split(" ")
        a = Moves.__getitem__(a)
        if b == "X":
            total_points += weight.get(loses.get(a))
        elif b == "Y":
            total_points += 3
            total_points += weight.get(a)
        else:
            total_points += 6
            total_points += weight.get(wins.get(a))

    return total_points


solve(2, 1, solution, lambda x: x, example, 15)
solve(2, 2, solution_2, lambda x: x, example, 12)
