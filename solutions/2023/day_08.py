from AoC.utils import solve
from math import lcm


example = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".splitlines()


example_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()


def make_network(puzzle_input: list[str]) -> tuple[tuple[int], dict[str, tuple[str]]]:
    instructions = tuple(int(i) for i in puzzle_input[0].replace("R", "1").replace("L", "0"))

    network = {}
    for paths in puzzle_input[2:]:
        name, exits = paths.split("=")
        network[name.strip()] = exits.replace(" ", "").strip("()").split(",")

    return instructions, network


def solution(puzzle_input: list[str]) -> int:
    instructions, network = make_network(puzzle_input)

    current = "AAA"
    steps = 0
    while current != "ZZZ":
        current = network[current][int(instructions[steps % len(instructions)])]
        steps += 1

    return steps


def solution_2(puzzle_input: list[str]) -> int:
    instructions, network = make_network(puzzle_input)

    current: list[str] = [i for i in network.keys() if i.endswith("A")]
    steps = 0
    total_steps = []

    while current:
        _currents = []
        for path in current:
            if path.endswith("Z"):
                total_steps.append(steps)
            else:
                _currents.append(network[path][int(instructions[steps % len(instructions)])])

        current = _currents
        steps += 1

    return lcm(*total_steps)


solve(8, 1, solution, lambda x: x, example, 2)
solve(8, 2, solution_2, lambda x: x, example_3, 6)
