from typing import Union
from AoC.utils import get_input


def most(value: int, half: int) -> int:
    """Returns 1 if value is more common than the other"""
    return 1 if value >= half else 0


def least(value: int, half: int) -> int:
    """Returns 1 if value is less common than the other"""
    return 1 if value < half else 0


def vertical_sum(iterable: list[list[int]], x: int) -> int:
    """Returns sum of vertical values in x column"""
    return sum([y[x] for y in iterable])


def apply(iterable: list[list[int]], common: Union[most, least] = None, y: int = 0, vertical: int = None) -> list[int]:
    """Reduces lists according to predicate till only one remains"""
    if len(iterable) == 1:
        return iterable[0]
    if common:
        vertical = common(vertical_sum(iterable, y), len(iterable) / 2)
    return apply(list(filter(lambda x: x[y] == vertical, iterable)), common, y + 1)


def toInt(iterable: list[int]) -> int:
    """Turns list of binary values into decimal value"""
    return int("0b" + "".join([str(i) for i in iterable]), base=0)


report = get_input(3, lambda x: [int(i) for i in list(x)])

most_common_bits = [vertical_sum(report, x) for x in range(len(report[0]))]
half = len(report) // 2
gamma = toInt([most(i, half) for i in most_common_bits])
epsilion = toInt([least(i, half) for i in most_common_bits])
print(gamma * epsilion)

generator_rating = toInt(apply(report, most))
scrubing_rating = toInt(apply(report, least))
print(generator_rating * scrubing_rating)
