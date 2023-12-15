from AoC.utils import solve


example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""".splitlines()


def hash(string: str) -> int:
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value


def solution(puzzle_input: list[str]) -> int:
    return sum([hash(step) for step in puzzle_input[0].strip().split(",")])


def solution_2(puzzle_input: list[str]) -> int:
    boxes = [{} for _ in range(256)]
    for step in puzzle_input[0].strip().split(","):
        if "=" in step:
            name, length = step.split("=")
        else:
            name, length = step.split("-")[0], 0

        label = hash(name)
        if length == 0:
            boxes[label].pop(name, None)
        else:
            boxes[label][name] = int(length)

    power = 0
    for x, box in enumerate(boxes, 0):
        for slot, length in enumerate(box.values(), 1):
            power += (1 + x) * slot * length

    return power


solve(15, 1, solution, lambda x: x, example, 1320)
solve(15, 2, solution_2, lambda x: x, example, 145)
