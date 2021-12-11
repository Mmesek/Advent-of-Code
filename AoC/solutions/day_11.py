class Octopus:
    energy: int = 0
    already_flashed: bool = False

    def __init__(self, energy: str) -> None:
        self.energy = int(energy)
        self.flashed_on = 0
        self.flash_count = 0

    def increase_energy(self, step: int) -> bool:
        if self.flashed_on != step:
            self.energy += 1
        if self.energy > 9 and self.flashed_on != step:
            self.energy = 0
            self.flashed_on = step
            self.flash_count += 1
            return True
        return False


def flash(x: int, y: int, matrix: list[list[Octopus]], step: int):
    if matrix[x][y].increase_energy(step):
        if x:
            flash(x - 1, y, matrix, step)
        if len(matrix[y]) - 1 > x:
            flash(x + 1, y, matrix, step)
        if y:
            if x:
                flash(x - 1, y - 1, matrix, step)
            flash(x, y - 1, matrix, step)
            if len(matrix[y]) - 1 > x:
                flash(x + 1, y - 1, matrix, step)
        if len(matrix) - 1 > y:
            if x:
                flash(x - 1, y + 1, matrix, step)
            flash(x, y + 1, matrix, step)
            if len(matrix[y]) - 1 > x:
                flash(x + 1, y + 1, matrix, step)


def iterate(iterable: list[list[Octopus]]) -> tuple[int, int]:
    all_flashed = []
    total_flashes = 0
    for step in range(500 + 1):
        for y, row in enumerate(iterable):
            for x, _ in enumerate(row):
                flash(x, y, iterable, step)
        if all([all(octop.energy == 0 for octop in row) for row in iterable]):
            all_flashed.append(step)
            if total_flashes:
                break
        if step == 100:
            total_flashes = sum([sum([i.flash_count for i in _]) for _ in iterable])
    return total_flashes, all_flashed[0]


from AoC.utils import get_input

print(iterate(get_input(11, lambda x: [Octopus(i) for i in x])))
