from AoC.utils import solve
from collections import defaultdict


example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    cwd = [""]
    tree = defaultdict(list)

    for cmd in puzzle_input:
        if cmd[0] != "$":
            path = "/".join(cwd)
            tree[path].append((cmd[0], path + "/" + cmd[1] if cmd[0] == "dir" else cmd[1]))
        elif cmd[1] == "cd":
            if cmd[-1] == "..":
                cwd.pop()
            elif cmd[-1] == "/":
                cwd = [""]
            else:
                cwd.append(cmd[-1])

    def calc_sum(directory):
        return sum([int(i[0] or 0) if i[0].isnumeric() else calc_sum(tree[i[1]]) for i in directory if i[0]])

    sizes = list(map(calc_sum, tree.values()))

    total_size = 0
    required = 30000000 - (70000000 - max(sizes))
    candidates = []

    for size in sizes:
        if size <= 100000:
            total_size += size
        if required <= size:
            candidates.append(size)

    return total_size, min(candidates)


solve(7, 1, solution, lambda x: x.split(), example, (95437, 24933642))
solve(7, 2, solution, lambda x: x.split(), example, (95437, 24933642))
