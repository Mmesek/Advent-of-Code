operators = {
    "inp": lambda x: x,
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: x // y,
    "mod": lambda x, y: x % y,
    "eql": lambda x, y: 1 if x == y else 0,
}


class ALU:
    def __init__(self, instructions: list[str] = None) -> None:
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
        if not instructions:
            instructions = global_instructions
        self.instructions = instructions
        self.current = 0

    def run(self, value: int):
        self.instructions[self.current]
        #ins, *var = self.instructions[self.current]
        match self.instructions[self.current]:
            case ["inp", a]:
                setattr(self, a, int(value))
            case [ins, a, b]:
                if not b.isdigit() and '-' not in b:
                    b = getattr(self, b)
                setattr(self, a, operators.get(ins)(getattr(self, a), int(b)))

        #if ins == "inp":
        #    setattr(self, var[0], int(value))
        #else:
        #    a, b = var
       #     if not b.isdigit() and "-" not in b:
       #         b = getattr(self, b)
       #     setattr(self, a, operators.get(ins)(getattr(self, a), int(b)))
        self.current += 1


def find_largest_model(instructions = None):
    for i in range(99999919656617, 10000000000000, -1):
        if "0" in str(i):
            continue
        x = 0
        program = ALU(instructions)
        for instruction in program.instructions:
            if program.instructions[program.current][0] == "inp":
                x += 1
            program.run(list(str(i))[x - 1])
        if program.z == 0:
            return i


from AoC.utils import get_input

global_instructions = get_input(24, lambda x: x.split(" "))
print(find_largest_model())
