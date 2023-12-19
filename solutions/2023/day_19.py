from AoC.utils import solve
import re

example = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""".splitlines()

pattern = re.compile(r"(\w+)?{(.*)}")


def parse(puzzle_input: list[str]) -> tuple[dict[str, tuple[int, str, int]], list[dict[str, int]]]:
    workflows = {}
    parts = []
    for line in puzzle_input:
        if not line:
            continue
        name, content = pattern.match(line).groups()
        content = content.split(",")
        if name:
            instructions = []
            for instr in content:
                if any(i in instr for i in "<>"):
                    condition, result = instr.split(":")
                    part, amount = condition.split("<") if "<" in condition else condition.split(">")
                    if "<" in condition:
                        condition = part, "<", int(amount)
                    elif ">" in condition:
                        condition = part, ">", int(amount)
                    instr = (condition, result)
                else:
                    instr = ((True, None, True), instr)
                instructions.append(instr)
            workflows[name] = instructions
        else:
            _parts = {}
            for i in content:
                k, v = i.split("=")
                _parts[k] = int(v)

            parts.append(_parts)

    return workflows, parts


def run(workflows, parts):
    workflow = "in"
    while workflow not in {"A", "R"}:
        for condition, result in workflows[workflow]:
            if (
                (condition[1] == "<" and parts[condition[0]] < condition[2])
                or (condition[1] == ">" and parts[condition[0]] > condition[2])
                or condition[1] == None
            ):
                workflow = result
                break
    if workflow == "A":
        return sum([i for i in parts.values()])


def solution(puzzle_input: list[str]) -> int:
    workflows, parts = parse(puzzle_input)
    accepted = []
    for _parts in parts:
        if r := run(workflows, _parts):
            accepted.append(r)

    return sum(accepted)


solve(19, 1, solution, lambda x: x, example, 19114)
