from AoC.utils import solve
from string import ascii_letters

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".splitlines()


def get_priority(items: list[str]):
    priority = 0

    for item in items:
        priority += ascii_letters.find(str(item)) + 1

    return priority


def solution(puzzle_input: list[str]) -> int:
    items = []

    for rucksack in puzzle_input:
        mid = len(rucksack) // 2
        items.extend(set(rucksack[:mid]).intersection(set(rucksack[mid:])))

    return get_priority(items)


def solution_2(puzzle_input: list[str]) -> int:
    items = []

    for group in zip(*[iter(puzzle_input)] * 3):
        items.extend(set(group[0]).intersection(*group[1:]))

    return get_priority(items)


solve(3, 1, solution, lambda x: x, example, 157)
solve(3, 2, solution_2, lambda x: x, example, 70)
