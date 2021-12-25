example: list[list[int]] = [
    [int(i.replace("[", "").replace("]", "")) for i in number.split(",")]
    for number in """[1,1]
[2,2]
[3,3]
[4,4]""".splitlines()
]


def explode(number: list[int]) -> list[list[int]]:
    pass


def split(number: list[list[int]]) -> list[list[int]]:
    pass


def add(numbers: list[list[int]]) -> list[list[int]]:
    pass


def magnitude(numbers: list[list[int]]) -> int:
    pass


assert add(example) == [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]
assert magnitude([[9, 1], [1, 9]]) == 129
assert magnitude([[1, 2], [[3, 4], 5]]) == 143

from AoC.utils import get_input

print(
    magnitude(
        add(
            get_input(18, 
            lambda x: [int(i.replace("[", "").replace("]", "")) for i in x.split(",")]
            )
        )
    )
)
