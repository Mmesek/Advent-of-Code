from AoC.utils import solve


example = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
""".splitlines()


def run(mapped):
    try_later = [monkey for monkey in mapped.keys()]

    while try_later:
        monkey = try_later.pop(0)
        try:
            exec(monkey + "=" + mapped[monkey])
        except NameError:
            try_later.append(monkey)

    return eval(mapped["root"])


def solution(puzzle_input: list[str]) -> int:
    return int(run({monkey: job for monkey, job in puzzle_input}))


def solution_2(puzzle_input: list[str]) -> int:
    mapped = {monkey: job for monkey, job in puzzle_input}
    mapped["root"] = mapped["root"].replace("+", ",").replace("*", ",").replace("-", ",").replace("/", ",")
    i = 0

    while True:
        mapped["humn"] = str(i)
        root = run(mapped)

        if root[0] == root[1]:
            print(i, root)
            break
        i += 1

    return i


solve(21, 1, solution, lambda x: x.split(": "), example, 152)
solve(21, 2, solution_2, lambda x: x.split(": "), example, 301)
