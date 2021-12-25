from typing import Any
from datetime import datetime


def get_input(day: int, func: callable = lambda i: i) -> list[Any]:
    """Retrieves input from a file calling `func` on each line"""
    try:
        with open(f"inputs/day{day}_input.txt", "r", newline="", encoding="utf-8") as file:
            lines = file.readlines()
    except IOError:
        lines = request_input(day)
    array = []
    for line in lines:
        array.append(func(line.strip()))
    return array


def request_input(day: int, year: int = datetime.now().year) -> list[str]:
    """Requests input from Advent of Code's website"""
    import requests

    print("REQUESTING", day)
    with open("cookie.dat", "r", newline="", encoding="utf-8") as file:
        cookie = file.readline()
    r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": cookie})
    with open(f"inputs/day{day}_input.txt", "w", newline="", encoding="utf-8") as file:
        file.writelines(r.text)
    return r.text.splitlines()

def check_answer(answer: int, day: int, part: int, year: int = datetime.now().year) -> bool:
    import requests
    with open("cookie.dat", "r", newline="", encoding="utf-8") as file:
        cookie = file.readline()
    r = requests.request("POST", f"https://adventofcode.com/{year}/day/{day}/answer", cookies={"session": cookie}, data=f"level={part}&answer={answer}",)
    return r.text.splitlines()

def solve(day: int, part: int, function: callable, preprocess: callable, example: str = None, expected_solution: int = None):
    if example and expected_solution:
        arr = []
        for line in example:
            arr.append(preprocess(line.strip()))
        r = function(arr)
        assert r == expected_solution, f"Solution for example doesn't match expected {expected_solution} example solution (got {r})"
    solution = function(get_input(day, preprocess))
    print(solution)
    #check_answer(solution, day, part)
