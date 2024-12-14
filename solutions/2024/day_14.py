import re
from dataclasses import dataclass
from AoC.utils import solve
from AoC.helpers import Grid, Coordinate

example = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".splitlines()


@dataclass
class Robot(Coordinate):
    velocity_x: int = 0
    velocity_y: int = 0

    def move(self):
        self.x += self.velocity_x
        if self.x > self.grid.length:
            self.x -= self.grid.length
        if self.x < 0:
            self.x += self.grid.length
        self.y += self.velocity_y
        if self.y > self.grid.height:
            self.y -= self.grid.height
        if self.y < 0:
            self.y += self.grid.height

    def quadrant(self):
        middle_x = self.grid.length // 2
        middle_y = self.grid.height // 2
        if self.x < middle_x and self.y < middle_y:
            return 0  # Top Left
        if self.x > middle_x and self.y < middle_y:
            return 1  # Top Right
        if self.x < middle_x and self.y > middle_y:
            return 2  # Bottom Left
        if self.x > middle_x and self.y > middle_y:
            return 3  # Bottom Right


PATTERN = re.compile(r"p=(\-?\d+),(\-?\d+) v=(\-?\d+),(\-?\d+)")


def parse(puzzle_input: list[str], grid: Grid) -> list[Robot]:
    robots = []
    for line in puzzle_input:
        px, py, vx, vy = PATTERN.findall(line)[0]
        robots.append(Robot(int(py), int(px), grid, int(vx), int(vy)))
    return robots


def solution(
    puzzle_input: list[str], seconds: int = 100, tall: int = 103, wide: int = 101
) -> int:
    g = Grid.pseudo_grid(tall, wide)
    robots = parse(puzzle_input, g)
    for second in range(seconds):
        for robot in robots:
            robot.move()
    quadrants = {i: [] for i in range(4)}
    quadrants[None] = []
    for robot in robots:
        quadrants[robot.quadrant()].append(robot)
    quadrants.pop(None)

    per_quadrant = [len(i) for i in quadrants.values()]
    r = 1
    for i in per_quadrant:
        if i:
            r *= i
    return r


solve(14, 1, solution, lambda x: x, example, 12, tall=7, wide=11)
