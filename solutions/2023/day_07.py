from AoC.utils import solve
from collections import Counter
from functools import cmp_to_key

example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

CARDS = [i.strip() for i in "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(",")]

TYPES = {
    7: (5,),
    6: (4, 1),
    5: (3, 2),
    4: (3, 1, 1),
    3: (2, 2, 1),
    2: (2, 1, 1, 1),
    1: (1, 1, 1, 1, 1),
}


def compare(a, b) -> int:
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    for x, card_a in enumerate(a[0]):
        card_b = b[0][x]
        if CARDS.index(card_a) > CARDS.index(card_b):
            return -1
        elif CARDS.index(card_a) < CARDS.index(card_b):
            return 1
    return 0


def solution(puzzle_input: list[tuple[str, str]]) -> int:
    bids = {hand: int(bid) for hand, bid in puzzle_input}
    hands = []

    for hand, _ in puzzle_input:
        _hand = tuple(sorted(Counter(hand).values(), reverse=True))
        for type, cards in TYPES.items():
            if _hand == cards:
                hands.append((hand, type))
                break

    hands = sorted(hands, key=cmp_to_key(compare))

    return sum([bids[i[0]] * x for x, i in enumerate(hands, 1)])


solve(7, 1, solution, lambda x: x.split(" "), example, 6440)
