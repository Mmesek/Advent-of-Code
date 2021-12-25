example = [[int(i) for i in line] for line in 
"""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".splitlines()]
cave = example

def find_lowest(x:int, y:int, matrix: list[list[int]], previous: int) -> list[int, int]:
    lowest = 10
    yx = [0,0]
    if len(matrix) - 1 > y and matrix[y+1][x] < lowest and [x, y+1] not in previous:
        lowest = matrix[y+1][x]
        yx = [y+1, x]
    if len(matrix[y]) - 1 > x and matrix[y][x+1] < lowest and [x+1, y] not in previous:
        lowest = matrix[y][x+1]
        yx = [y, x+1]
    if x and matrix[y][x-1] < lowest and [x-1, y] not in previous:
        lowest = matrix[y][x-1]
        yx = [y, x-1]
    if y and matrix[y-1][x] < lowest and [x, y-1] not in previous:
        lowest = matrix[y-1][x]
        yx = [y-1, x]
    if yx == [0,0]:
        raise Exception
    return yx

# https://www.pythonpool.com/a-star-algorithm-python/
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# https://arongranberg.com/astar/
# https://media.discordapp.net/attachments/910196070729015346/921161522875617280/unknown.png?width=675&height=641
# https://nedbatchelder.com/text/bigo.html

class Node:
    def __init__(self, x, y, target_x, target_y, matrix, previous) -> None:
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.previous = previous
        self.danger = matrix[y][x]

    @property
    def x_diff(self):
        return self.target_x - self.x

    @property
    def y_diff(self):
        return self.target_y - self.y
    
    @property
    def cost(self) -> int:
        return self.danger + (self.x_diff + self.y_diff) # Closest to OG Path, 52 risk
        return self.danger + (self.x_diff + self.y_diff)**2 # Mirrored, 44 risk, Doesn't reach final destination
        return self.danger * (self.x_diff + self.y_diff)**2 # Closest to OG Path, 52 risk
        return self.danger + (self.x_diff ** self.y_diff) # Drunk Tunnel x/y, 55 risk
        return self.danger * (self.x_diff ** self.y_diff) # Tunnel x/y, 58 risk
        return self.danger + (self.x_diff ** self.y_diff)*2 # Tunnel x/y Drunk at the end, 57 risk
        return self.danger + (self.x_diff**2 + self.y_diff**2) # Straight, 45 risk
        return self.danger * (self.x_diff**2 + self.y_diff**2) # Closest to OG Path, 52 risk

    def nodes(self, matrix) -> list['Node']:
        nodes = []
        this = (self.x, self.y)
        if self.x and (self.x-1, self.y) != self.previous:
            nodes.append(Node(self.x-1, self.y, self.target_x, self.target_y, matrix, this))
        if self.y and (self.x, self.y-1) != self.previous:
            nodes.append(Node(self.x, self.y-1, self.target_x, self.target_y, matrix, this))
        if len(matrix) - 1 > self.y and (self.x, self.y+1) != self.previous:
            nodes.append(Node(self.x, self.y+1, self.target_x, self.target_y, matrix, this))
        if len(matrix[self.y]) - 1 > self.x and (self.x+1, self.y) != self.previous:
            nodes.append(Node(self.x+1, self.y, self.target_x, self.target_y, matrix, this))
        return nodes

target_y = len(cave) - 1
target_x = len(cave[target_y]) -1

path = []
n = Node(0, 0, target_y, target_x, cave, (0,0))
expected_path = [
#    x, y
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (3, 2),
    (4, 2),
    (5, 2),
    (6, 2),
    (6, 3),
    (7, 3),
    (7, 4),
    (7, 5),
    (8, 5),
    (8, 6),
    (8, 7),
    (8, 8),
    (9, 8),
    (9, 9),
]
visited = set()
break_next = False
while True:
    path.append(n)
    nodes = sorted([node for node in n.nodes(cave)], key=lambda x: x.cost)
    n = next(filter(lambda x: (x.x, x.y) not in visited, nodes), None)
    if not n:
        p = path.pop()
        #p = path.pop(-1)
        visited.remove((p.x, p.y))
        #n = nodes[-1]
        n = next(iter(nodes))
    print([i.danger for i in nodes], n.danger)
    for node in nodes:
        visited.add((node.x, node.y))
    #print(n.cost)
    visited.add((n.x, n.y))
    if break_next:
        break
    if n.x == target_x and n.y == target_y:
    #if n.cost <= 1:
        break_next = True


def print_map(path):
    graph = {i:[' . ' for _ in range(10)] for i in range(10)}
    for _, i in enumerate(path):
        if type(i) is Node:
            y = i.y
            if len(expected_path) > _ and y != expected_path[_][1]:
                graph[expected_path[_][1]][expected_path[_][0]] = ' x '
                print(f"Expected y {expected_path[_][1]} but received {y} at {_}")
            x = i.x
            if len(expected_path) > _ and x != expected_path[_][0]:
                graph[expected_path[_][1]][expected_path[_][0]] = ' * '
                print(f"Expected x {expected_path[_][0]} but received {x} at {_}")
            danger = i.danger
        else:
            y = i[1]
            x = i[0]
            danger = _
        graph[y][x] = f"{danger:^3}"
    print("  |"," ".join([f"{i:^3}" for i in range(10)]))
    print("  |","--- "*10)
    for r, i in graph.items():
        print(r,"|", " ".join(i))

print_map(path)

print("Path length:", len(path))
print("Total risk:", sum([i.danger for i in path]))

#total_risk = 0
#path = [[0,0]]
#while True:
#    y, x = find_lowest(x, y, cave, path)
#    path.append([x,y])
#    total_risk += cave[y][x]
#    if len(cave) == y and len(cave[y]) == x:
#        break
#print(total_risk)
