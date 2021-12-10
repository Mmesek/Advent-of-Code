from AoC.utils import get_input

mapping = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
r_mapping = {v: k for k, v in mapping.items()}

cost = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores = {")": 1, "]": 2, "}": 3, ">": 4}


def find_errors(lines: list[str]) -> tuple[int, int]:
    illegal_chars = []
    autocompleted = []
    for line in lines:
        line_discarded = False
        last_open_scope = []
        for char in line:
            if char in mapping.keys():
                last_open_scope.append(char)
            elif char in mapping.values():
                if r_mapping[char] == last_open_scope[-1]:
                    last_open_scope.pop()
                else:
                    illegal_chars.append(char)
                    line_discarded = True
                    break
        if not line_discarded:
            score = 0
            for unclosed in last_open_scope[::-1]:
                score *= 5
                score += scores[mapping[unclosed]]
            autocompleted.append(score)
    p1 = sum([cost[i] for i in illegal_chars])
    p2 = sorted(autocompleted)[len(autocompleted) // 2]
    return p1, p2


print(find_errors(get_input(10)))
