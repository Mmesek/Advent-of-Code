from AoC.utils import solve

example = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""".splitlines()


class Node:
    def __init__(self, x: int, y: int, a: tuple[int], b: tuple[int]) -> None:
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.from_start: int = None


PIPES = {
    "|": lambda x, y: Node(x, y, (x, y - 1), (x, y + 1)),
    "-": lambda x, y: Node(x, y, (x - 1, y), (x + 1, y)),
    "L": lambda x, y: Node(x, y, (x, y - 1), (x + 1, y)),
    "J": lambda x, y: Node(x, y, (x, y - 1), (x - 1, y)),
    "7": lambda x, y: Node(x, y, (x, y + 1), (x - 1, y)),
    "F": lambda x, y: Node(x, y, (x, y + 1), (x + 1, y)),
}


def get_node(grid: dict[tuple[int], Node], x: int, y: int, target: tuple[int]) -> Node:
    if (x, y) not in grid:
        return
    if grid[x, y].a == target or grid[x, y].b == target:
        return grid[x, y]


def clean(grid: dict[tuple[int], Node]) -> dict[tuple[int], Node]:
    to_strip = []
    for node in grid:
        if node in grid and grid[node].a in grid and grid[node].b in grid:
            grid[node].a = grid[grid[node].a]
            grid[node].b = grid[grid[node].b]
        else:
            to_strip.append(node)
    for node in to_strip:
        grid.pop(node)
    return grid


def find_start(grid: dict[tuple[int], Node], start: tuple[int]) -> Node:
    x = start[0]
    y = start[1]
    node_a = None

    if node := get_node(grid, x + 1, y, start):
        node_a = node
    if node := get_node(grid, x - 1, y, start):
        if node_a:
            node_b = node
        else:
            node_a = node
    if node := get_node(grid, x, y + 1, start):
        if node_a:
            node_b = node
        else:
            node_a = node
    if node := get_node(grid, x, y - 1, start):
        if node_a:
            node_b = node
        else:
            node_a = node

    return Node(x, y, (node_a.x, node_a.y), (node_b.x, node_b.y))


def make_grid(puzzle_input: list[str]) -> tuple[tuple[int], dict[tuple[int], Node]]:
    grid = {}
    for y, line in enumerate(puzzle_input):
        for x, node in enumerate(line):
            if node in PIPES:
                grid[(x, y)] = PIPES[node](x, y)
            elif node == "S":
                start = x, y

    grid[start] = find_start(grid, start)
    return start, clean(grid)


def find_furthest_point(node_a: Node, node_b: Node) -> int:
    steps = 0
    node = node_a
    traversed = [node_a]

    while True:
        steps += 1
        node = node.a if node.a not in traversed else node.b
        traversed.append(node)
        node.from_start = steps
        if node == node_b:
            break

    steps = 0
    node = node_b
    traversed = [node_b]
    while True:
        steps += 1
        node = node.b if node.b not in traversed else node.a
        traversed.append(node)
        if node.from_start == steps:
            steps = node.from_start
            break

    return steps + 1


def solution(puzzle_input: list[str]) -> int:
    start, grid = make_grid(puzzle_input)
    return find_furthest_point(grid[start].a, grid[start].b)


solve(10, 1, solution, lambda x: x, example, 8)
