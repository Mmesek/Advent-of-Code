from AoC.utils import solve
from itertools import zip_longest

example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".splitlines()


class Value:
    def __init__(self, start: int, source: int, length: int) -> None:
        self.start = int(start)
        self.source = int(source)
        self.length = int(length) - 1

    def __contains__(self, value: int) -> bool:
        if self.source <= value <= self.source + self.length:
            return True
        return False

    def __getitem__(self, value: int) -> int:
        return self.start + value - self.source


def make_maps(puzzle_input: list[str]) -> dict[str, list[Value]]:
    maps: dict[str, list[Value]] = {}
    curr_map = ""
    for line in puzzle_input[1:]:
        if not line:
            curr_map = ""
        elif curr_map:
            maps[curr_map].append(Value(*line.split(" ")))
        elif ":" in line:
            curr_map = line.split(" ")[0]
            maps[curr_map] = []

    return maps


def solution(maps: dict[str, list[Value]], seeds: list[int]) -> int:
    locations = []
    for seed in seeds:
        value = seed
        for map in maps.values():
            for range in map:
                if value in range:
                    value = range[value]
                    break
        locations.append(value)
    return min(locations)


def part_1(puzzle_input: list[str]):
    seeds = [int(i) for i in puzzle_input[0].split(": ")[-1].split(" ")]
    maps = make_maps(puzzle_input)
    return solution(maps, seeds)


def part_2(puzzle_input: list[str]):
    _seeds = [int(i) for i in puzzle_input[0].split(": ")[-1].split(" ")]
    seeds = []

    maps = make_maps(puzzle_input)
    for a, b in zip_longest(*[iter(_seeds)] * 2):
        for i in range(a, a + b):
            seeds.append(i)

    return solution(maps, seeds)


solve(5, 1, part_1, lambda x: x, example, 35)
# solve(5, 2, part_2, lambda x: x, example, 46)
