from AoC.utils import solve

example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()


def preprocess(line: str) -> tuple[int, str]:
    card, numbers = line.split(":")
    card = int(card.split()[-1])
    winning, guessed = numbers.split("|")
    winning = winning.strip().split()
    guessed = guessed.strip().split()
    return card, len([number for number in guessed if number in winning])


def solution(puzzle_input: list[tuple[int, str]]) -> int:
    total = 0
    for _, correct in puzzle_input:
        points = 0

        for _ in range(correct):
            if not points:
                points = 1
            else:
                points *= 2

        total += points
    return total


def solution_2(puzzle_input: list[tuple[int, str]]) -> int:
    cards = {k: v for k, v in puzzle_input}
    counts = {k: 1 for k in cards}

    for card, correct in cards.items():
        for duplicate in range(counts[card]):
            for x in range(1, correct + 1):
                if card + x in counts:
                    counts[card + x] += 1

    return sum(counts.values())


solve(4, 1, solution, preprocess, example, 13)
solve(4, 2, solution_2, preprocess, example, 30)
