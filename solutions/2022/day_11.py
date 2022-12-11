from AoC.utils import solve


example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".splitlines()


class Monkey:
    inspection_counter: int
    inventory: list[int]
    operation: str
    test: int
    true: int
    false: int

    def __init__(self) -> None:
        self.inspection_counter = 0


def solution(puzzle_input: list[str], rounds: int = 20, divide_by=3) -> int:
    monkeys: list[Monkey] = []
    product = 1
    for k, v in [line.split(":") for line in puzzle_input if line]:
        if k.split()[0] == "Monkey":
            monkeys.append(Monkey())
        elif k == "Starting items":
            monkeys[-1].inventory = [int(i) for i in v.split(",")]
        elif k == "Operation":
            monkeys[-1].operation = v.split("=")[-1].strip()
        elif k == "Test":
            monkeys[-1].test = int(v.split(" ")[-1])
            product *= monkeys[-1].test
        elif k == "If true":
            monkeys[-1].true = int(v.split(" ")[-1])
        elif k == "If false":
            monkeys[-1].false = int(v.split(" ")[-1])

    for _ in range(rounds):
        for monkey in monkeys:
            for item in list(monkey.inventory):
                monkey.inspection_counter += 1
                item = (eval(monkey.operation.replace("old", str(item))) % product) // divide_by
                monkeys[monkey.false if item % monkey.test else monkey.true].inventory.append(item)

            monkey.inventory.clear()

    top = sorted(monkeys, key=lambda x: x.inspection_counter, reverse=True)[:2]

    return top[0].inspection_counter * top[1].inspection_counter


solve(11, 1, solution, lambda x: x, example, 10605)
solve(11, 2, solution, lambda x: x, example, 2713310158, rounds=10000, divide_by=1)
