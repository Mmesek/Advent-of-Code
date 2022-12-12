from AoC.utils import solve
from string import ascii_lowercase

example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()


class Node:
    def __init__(self, x: int, y: int, height: int) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.parent = None

    def neighbour(self, node: "Node") -> bool:
        return (
            (
                (abs(self.x - node.x) <= 1 and abs(self.y - node.y) == 0)
                or (abs(self.x - node.x) <= 0 and abs(self.y - node.y) <= 1)
            )
            and (self.height - node.height) <= 1
            and node != self
        )


def dijkstra(matrix: list["Node"], start: Node, end: Node) -> int:
    queue = [start]

    for node in matrix:
        node.parent = None

    visited = set()

    while queue:
        node = queue.pop(0)
        visited.add(node)
        neighbours = [n for n in matrix if n.neighbour(node) and n not in visited]

        for neighbour in neighbours:
            neighbour.parent = node

            if neighbour not in queue:
                queue.append(neighbour)

    steps = 0

    if not end.parent:
        return None

    node = end

    while node != start:
        steps += 1
        node = node.parent

    return steps


def solution(puzzle_input: list[str], starts_at: set = {"S"}) -> int:
    possible_start, matrix, steps = [], [], []
    end = None

    for x, row in enumerate(puzzle_input):
        for y, char in enumerate(row):
            if char in starts_at:
                matrix.append(Node(x, y, 0))
                possible_start.append(matrix[-1])
            elif char.islower():
                matrix.append(Node(x, y, ascii_lowercase.find(char)))
            elif char == "E":
                matrix.append(Node(x, y, 25))
                end = matrix[-1]

    for start in possible_start:
        steps.append(dijkstra(matrix, start, end))

    return min([i for i in steps if i])


solve(12, 1, solution, lambda x: x, example, 31)
solve(12, 2, solution, lambda x: x, example, 29, starts_at={"S", "a"})
