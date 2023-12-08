from AoC.utils import solve
from collections import Counter
from functools import cmp_to_key

example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

CARDS = [i.strip() for i in "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(",")]
CARDS_2 = [i.strip() for i in "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(",")]

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


def check_wildcards(_hand: tuple[int], cards: tuple[int], wildcards: int):
    if wildcards == 5:
        return True

    for x in range(len(_hand)):
        replaced = [i for i in _hand]
        replaced[x] += wildcards
        if tuple(replaced) == cards:
            return True

    replaced = [i for i in _hand]
    _wildcards = wildcards

    for x in range(len(_hand)):
        if _wildcards:
            replaced[x] += 1
            _wildcards -= 1
        if tuple(replaced) == cards:
            return True


def solution(puzzle_input: list[tuple[str, str]], wildcards: bool = False) -> int:
    bids = {hand: int(bid) for hand, bid in puzzle_input}
    hands = []
    if wildcards:
        global CARDS
        CARDS = CARDS_2

    for hand, _ in puzzle_input:
        _hand = tuple(sorted(Counter(hand.replace("J", "") if wildcards else hand).values(), reverse=True))
        for type, cards in TYPES.items():
            if wildcards and (_wildcards := hand.count("J")) > 0:
                if check_wildcards(_hand, cards, _wildcards):
                    hands.append((hand, type))
                    break

            if _hand == cards:
                hands.append((hand, type))
                break

    hands = sorted(hands, key=cmp_to_key(compare))

    return sum([bids[i[0]] * x for x, i in enumerate(hands, 1)])


solve(7, 1, lambda x: solution(x), lambda x: x.split(" "), example, 6440)
solve(7, 2, lambda x: solution(x, True), lambda x: x.split(" "), example, 5905)
