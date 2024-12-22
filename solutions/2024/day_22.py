from AoC.utils import solve
from functools import cache
from itertools import pairwise

example = """1
10
100
2024""".splitlines()


@cache
def multiply(number):
    number ^= number * 64
    return number % 16777216


@cache
def divide(number):
    number ^= number // 32
    return number % 16777216


@cache
def final(number):
    number ^= number * 2048
    return number % 16777216


@cache
def evolve(number):
    return final(divide(multiply(number)))


def solution(puzzle_input: list[str]) -> int:
    numbers = []
    for line in puzzle_input:
        n = int(line)
        for i in range(2000):
            n = evolve(n)
        numbers.append(n)
    return sum(numbers)


def solution_2(puzzle_input: list[str]) -> int:
    numbers = []
    for line in puzzle_input:
        n = int(line)
        secrets = [int(line[-1])]
        for i in range(2000):
            n = evolve(n)
            secrets.append(int(str(n)[-1]))
        numbers.append(secrets)

    buyers = []
    for buyer in numbers:
        changes = []
        for a, b in pairwise(buyer):
            changes.append(str(b - a))
        buyers.append(" ".join(changes))

    highest = {}
    for x, buyer in enumerate(buyers):
        scores = {}
        buyer = buyer.split(" ")
        for a, b, c, d, score in zip(
            buyer, buyer[1:], buyer[2:], buyer[3:], numbers[x][4:]
        ):
            sequence = " ".join([str(i) for i in [a, b, c, d]])
            _score = int(score)
            # for second in numbers:
            #    if sequence in second:
            #        _score += int(second.split(sequence, 1)[-1].split(" ", 1)[0])
            if _score:
                scores[(a, b, c, d)] = _score
        highest[x] = sorted(scores.items(), key=lambda x: x[1])[-1]
    return sorted(highest.values(), key=lambda x: x[1])[-1]


solve(22, 1, solution, lambda x: x, example, 37327623)
solve(22, 2, solution_2, lambda x: x, ["1", "2", "3", "2024"], 23)
