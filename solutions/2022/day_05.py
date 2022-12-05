from AoC.utils import solve
from collections import defaultdict

example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines()


def solution(puzzle_input: list[str], part_2: bool = False) -> str:
    idx = {}
    crates = defaultdict(list)
    instructions = False

    for line in puzzle_input:
        if not line.strip():
            for crate in crates:
                crates[crate].reverse()
            instructions = True
        elif not instructions:
            for x, char in enumerate(line):
                if char.isalpha():
                    crates[x].append(char)
                elif char.isnumeric():
                    idx[char] = x
        else:
            _, move, _, start, _, end = line.strip().split(" ")

            moved = [crates[idx[start]].pop() for _ in range(int(move))]
            if part_2:
                moved.reverse()

            crates[idx[end]].extend(moved)

    return "".join([crates[crate][-1] for crate in sorted(crates)])


def solution_2(puzzle_input: list[str]) -> str:
    return solution(puzzle_input, True)


solve(5, 1, solution, lambda x: x, example, "CMZ", strip=False)
solve(5, 2, solution_2, lambda x: x, example, "MCD", strip=False)
