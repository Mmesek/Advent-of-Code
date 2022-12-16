from AoC.utils import solve
from collections import defaultdict
from itertools import product
from functools import cache

example = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
""".splitlines()


def parse(puzzle_input: list[str]) -> tuple[dict[str, int], dict[str, list[str]]]:
    valves = {}
    paths = defaultdict(lambda: 1000)

    for line in puzzle_input:
        current, towards = line.split(";")
        name, rate = current.split("=")
        name = name.split()[1]
        valves[name] = int(rate)

        for i in towards.split("valve")[-1].split():
            if i != "s":
                paths[name, i.strip(",")] = 1

    return valves, paths


class Graph:
    def __init__(self, puzzle_input: list[str]) -> None:
        self.valves, self.paths = parse(puzzle_input)
        for k, i, j in product(self.valves, self.valves, self.valves):
            self.paths[i, j] = min(self.paths[i, j], self.paths[i, k] + self.paths[k, j])

    @cache
    def search(self, minutes: int, path: str, to_visit: frozenset, has_help: bool = False) -> int:
        _valves = []

        for valve in to_visit:
            if valve != path and self.paths[path, valve] < minutes:
                _valves.append(
                    self.valves[valve] * (minutes - self.paths[path, valve] - 1)
                    + self.search(minutes - self.paths[path, valve] - 1, valve, to_visit - {valve}, has_help)
                )

        if has_help:
            _valves.append(self.search(26, "AA", to_visit))

        return max(_valves + [0])


def solution(puzzle_input: list[str], minutes: int = 30, with_help: bool = False) -> int:
    g = Graph(puzzle_input)
    return g.search(minutes, "AA", frozenset([k for k, v in g.valves.items() if v]), with_help)


solve(16, 1, solution, lambda x: x, example, 1651)
solve(16, 2, solution, lambda x: x, example, 1707, minutes=26, with_help=True)
