from AoC.utils import solve
from dataclasses import dataclass
from math import pow

example = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""".splitlines()

example_2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""".splitlines()


@dataclass
class Device:
    a: int = 0
    b: int = 0
    c: int = 0
    steps: list[int] = list
    pointer: int = 0
    is_increased: bool = True
    initial_b: int = 0
    initial_c: int = 0

    @classmethod
    def from_input(cls, puzzle: list[str]):
        device = Device()
        for line in puzzle:
            if line.startswith("Register A"):
                device.a = int(line.split(": ")[-1])
            elif line.startswith("Register B"):
                device.initial_b = int(line.split(": ")[-1])
            elif line.startswith("Register C"):
                device.initial_c = int(line.split(": ")[-1])
            elif line.startswith("Program"):
                device.steps = [int(i) for i in line.split(": ")[-1].split(",")]
        device.reinitialize()
        return device

    def reinitialize(self):
        self.b = self.initial_b
        self.c = self.initial_c
        self.pointer = 0
        self.is_increased = True

    def opcode(self, op: int, operand: int):
        match op:
            case 0:
                self.a = int(self.a / pow(2, self.combo(operand)))
            case 1:
                self.b ^= operand
            case 2:
                self.b = self.combo(operand) % 8
            case 3:
                if self.a == 0:
                    return
                self.pointer = operand
                self.is_increased = True
            case 4:
                self.b ^= self.c
            case 5:
                return self.combo(operand) % 8
            case 6:
                self.b = int(self.a / pow(2, self.combo(operand)))
            case 7:
                self.c = int(self.a / pow(2, self.combo(operand)))

    def combo(self, operand: int):
        if operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        elif operand == 7:
            return
        return operand

    def next(self):
        if not self.is_increased:
            self.pointer += 2
            self.is_increased = True
        if self.pointer + 1 > len(self.steps):
            return None, None
        return self.steps[self.pointer], self.steps[self.pointer + 1]

    def run(self):
        out = []
        while self.pointer < len(self.steps):
            op, operand = self.next()
            if op is None:
                break
            self.is_increased = False
            if (o := self.opcode(op, operand)) is not None:
                out.append(o)
                if out[0] != self.steps[0]:
                    return
        return out


def solution(puzzle_input: list[str]) -> int:
    device = Device.from_input(puzzle_input)
    out = device.run()
    return ",".join([str(i) for i in out])


def solution2(puzzle_input: list[str]) -> int:
    device = Device.from_input(puzzle_input)
    x = -1
    out = 0
    while out != device.steps:
        x += 1
        device.a += x
        device.reinitialize()
        out = device.run()
    return x


solve(17, 1, solution, lambda x: x, example, "4,6,3,5,6,3,5,2,1,0")
solve(17, 2, solution2, lambda x: x, example_2, 117440)
