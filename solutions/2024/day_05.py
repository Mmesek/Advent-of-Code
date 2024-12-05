from AoC.utils import solve
from itertools import pairwise
from statistics import median
from collections import defaultdict

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".splitlines()


def is_valid(instruction: list[int], rules: dict[int, list[int]]):
    ok = True
    for a, b in pairwise(instruction):
        if b in rules[a]:
            continue
        if a in rules[b]:
            ok = False
    return ok


def solution(puzzle_input: list[str]) -> int:
    rules = defaultdict(set)
    simple_rules = []
    instructions = []
    ins_on = False
    for line in puzzle_input:
        if line == "":
            ins_on = True
        elif ins_on:
            instructions.append([int(i) for i in line.split(",")])
        else:
            a, b = line.split("|")
            a, b = int(a), int(b)
            simple_rules.append((a, b))
            rules[a].add(b)
    valid = []
    not_valid = []
    for each in instructions:
        if is_valid(each, rules):
            valid.append(each)
        else:
            not_valid.append(fix(each, simple_rules))
    middle, middle_2 = [], []
    for v in valid:
        middle.append(v[len(v) // 2])
    for v in not_valid:
        middle_2.append(v[len(v) // 2])

    return sum(middle), sum(middle_2)


def fix(instruction: list[int], rules: list[tuple[int, int]]):
    valid = True
    for a, b in rules:
        if a not in instruction or b not in instruction:
            continue
        x = instruction.index(a)
        y = instruction.index(b)
        if x > y:
            valid = False
            instruction[x], instruction[y] = instruction[y], instruction[x]

    if valid:
        return instruction
    return fix(instruction, rules)


solve(5, 1, solution, lambda x: x, example, (143, 123))
solve(5, 2, solution, lambda x: x, example, (143, 123))
