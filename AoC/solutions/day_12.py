from typing import DefaultDict
from AoC.utils import get_input

paths = get_input(12, lambda x: x.split("-"))
maps: dict[str, str] = DefaultDict(lambda: set())

for a, b in paths:
    maps[a].add(b)
    maps[b].add(a)

def walk(paths: list[str], visited: list[str], revisit: bool = False) -> list[list[str]]:
    branches = []
    for path in paths:
        if path == "end":
            branches.append(visited+[path])
            continue
        if path not in visited or path.isupper() or (revisit and path not in {"start","end"} and len(maps[path]) >= 1 and visited.count(path) <= 1):
            branches.append(visited+[path])
            r = walk(maps[path], visited+[path], revisit)
            if r:
                branches.append(r)
    return branches

w = walk(maps["start"], ["start"])

def clean(ls: list[list[str]], cleaned: list[str]) -> None:
    for j in ls:
        if type(j) is list:
            clean(j, cleaned)
        else:
            if ls[-1] == "end":
                cleaned.append(ls)
            break

cleaned = []
clean(w, cleaned)
print(len(cleaned))
