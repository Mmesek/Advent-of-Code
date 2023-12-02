from AoC.utils import solve
from collections import Counter

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()


def solution(puzzle_input: list[str], cubes: dict[str, int]) -> int:
    possible = 0

    for line in puzzle_input:
        game, _cubes = line.split(":")
        game_id = game.split()[-1]
        sets = _cubes.split(";")
        counters = []

        for _set in sets:
            counts = [i.strip().split() for i in _set.split(",")]
            counters.append(Counter({i[1]: int(i[0]) for i in counts}))

        if all(
            c["red"] <= cubes["red"] and c["blue"] <= cubes["blue"] and c["green"] <= cubes["green"] for c in counters
        ):
            possible += int(game_id)
    return possible


def solution_2(puzzle_input: list[str]) -> int:
    powers = 0
    for line in puzzle_input:
        top = Counter()

        _, _cubes = line.split(":")
        sets = _cubes.split(";")

        for _set in sets:
            counts = [i.strip().split() for i in _set.split(",")]
            for amount, color in counts:
                if top[color] < int(amount):
                    top[color] = int(amount)
        powers += top["red"] * top["green"] * top["blue"]

    return powers


solve(2, 1, lambda x: solution(x, Counter({"red": 12, "green": 13, "blue": 14})), lambda x: x, example, 8)
solve(2, 1, solution_2, lambda x: x, example, 2286)
