from AoC.utils import solve
from collections import defaultdict

example = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    connections: dict[str, str] = defaultdict(set)
    for line in puzzle_input:
        a, b = line.split("-")
        connections[a].add(b)
        connections[b].add(a)

    groups = set()
    for a in connections:
        connected_a = set([a])
        for b in connections[a]:
            connected_ab = set([a, b])
            connected_ac = set([a])
            for c in connections[b]:
                if c in connections[a]:
                    connected_a.add(c)
                    connected_ab.add(c)
                    connected_ac.add(c)

            if len(connected_ab) == 3:
                groups.add(tuple(sorted(connected_ab)))
            if len(connected_ac) == 3:
                groups.add(tuple(sorted(connected_ac)))
        if len(connected_a) == 3:
            groups.add(tuple(sorted(connected_a)))
    groups = sorted(list(groups))

    return len(list(filter(lambda x: any(i.startswith("t") for i in x), groups)))


solve(23, 1, solution, lambda x: x, example, 7)
