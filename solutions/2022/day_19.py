from AoC.utils import solve


example = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
""".splitlines()


class Cost:
    ore: int
    clay: int
    obsidian: int


class Blueprint:
    ore: Cost
    clay: Cost
    obsidian: Cost
    geode: Cost


class Factory:
    ore: int
    clay: int
    obsidian: int
    geode: int

    def __init__(self, blueprint, minutes=24):
        pass


def parse(puzzle_input):
    blueprints = {}
    for blueprint in puzzle_input:
        number, costs = blueprint.split(":")
        blueprints[number] = Blueprint(*[Cost(i) for i in costs.split(".")])


def solution(puzzle_input: list[str]) -> int:
    return 0


solve(19, 1, solution, lambda x: x, example, 33)
