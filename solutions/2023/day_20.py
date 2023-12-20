from AoC.utils import solve
from dataclasses import dataclass
from collections import defaultdict


example = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output""".splitlines()


@dataclass
class Module:
    name: str = "None"
    destinations: list[str] = list
    high: int = 0
    low: int = 0
    _state: bool = False

    def __post_init__(self):
        if type(self.destinations) is type:
            self.destinations = []

    @property
    def state(self) -> bool:
        return self._state

    def send(self, modules: dict[str, "Module"]) -> list[str]:
        _con = []
        for module in self.destinations:  # pylint: disable=not-an-iterable
            if modules[module].receive(self.state, self.name):
                _con.append(module)

        return _con

    def receive(self, pulse: bool, source: str = None) -> bool:
        if pulse:
            self.high += 1
        else:
            self.low += 1
        return True


@dataclass
class FlipFlop(Module):
    def receive(self, pulse: bool, source: str) -> bool:
        super().receive(pulse, source)
        if not pulse:
            self._state = not self._state
            return True


@dataclass
class Conjunction(Module):
    sources: dict[str, bool] = dict

    def __post_init__(self):
        if type(self.sources) is type:
            self.sources = {}
        return super().__post_init__()

    def receive(self, pulse: bool, source: str) -> bool:
        self.sources[source] = pulse  # pylint: disable=unsupported-assignment-operation
        return super().receive(pulse, source)

    def send(self, modules: dict[str, Module]) -> list[str]:
        if all(self.sources.values()) == False or all(self.sources.values()) == True:
            return super().send(modules)

    @property
    def state(self) -> bool:
        if all(self.sources.values()) in {True, False}:
            return not all(self.sources.values())


def prepare(puzzle_input: list[tuple[str]]) -> tuple[defaultdict[str, Module], defaultdict[str, list[str]]]:
    modules = defaultdict(Module)
    inputs = defaultdict(list)
    for module, destinations in puzzle_input:
        _type = module[0]
        module = module.strip().strip("%&")

        destinations = [i.strip() for i in destinations.split(",")]
        for destination in destinations:
            inputs[destination].append(module)

        if _type == "%":
            modules[module] = FlipFlop(module, destinations)
        elif _type == "&":
            modules[module] = Conjunction(module, destinations)
        else:
            modules[module] = Module(module, destinations)

    for name, module in modules.items():
        if type(module) is Conjunction:
            module.sources = {m: False for m in inputs[name]}

    return modules, inputs


def push_button(modules):
    modules["broadcaster"].receive(False, "button")
    queue = ["broadcaster"]
    while queue:
        queue.extend(modules[queue.pop(0)].send(modules))


def solution(puzzle_input: list[tuple[str]], button_presses: int = 1) -> int:
    modules, _ = prepare(puzzle_input)

    for _ in range(button_presses):
        push_button(modules)

    return sum([m.high for m in modules.values()]) * sum([m.low for m in modules.values()])


solve(20, 1, lambda x: solution(x, 1000), lambda x: x.split("->"), example, 11687500)
