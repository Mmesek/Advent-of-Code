from AoC.utils import solve
from copy import copy
from itertools import product

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()


def parse(puzzle_input):
    puzzle = []
    outcomes = []
    for line in puzzle_input:
        output, values = line.split(": ")
        outcomes.append(int(output))
        puzzle.append([int(v) for v in values.split(" ")])
    return puzzle, outcomes


def solution(puzzle_input: list[str], concat: bool = False) -> int:
    puzzle_input, outcomes = parse(puzzle_input)

    correct = 0
    for output, values in zip(outcomes, puzzle_input):
        for combo in product("+*|", repeat=len(values) - 1):
            vals = copy(values)
            for x, (op, b) in enumerate(zip(combo, vals[1:]), 1):
                a = vals[x - 1]
                b = vals[x]
                if op == "+":
                    vals[x] = a + b
                elif concat and op == "|":
                    vals[x] = int(str(a) + str(b))
                else:
                    vals[x] = a * b
            if sum(vals[1:]) == output:
                correct += sum(vals[1:])
                break
            elif vals[-1] == output:
                correct += vals[-1]
                break

    return correct


solve(7, 1, solution, lambda x: x, example, 3749)
solve(7, 2, solution, lambda x: x, example, 11387, concat=True)
