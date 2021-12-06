from AoC.utils import get_input
initial_fishes = get_input(6, lambda x: [int(i) for i in x.split(',')])[0]

class Fishes:
    def __init__(self) -> None:
        self.day = 1
        self.fishes = [0] * 9
        self.add_fishes(initial_fishes)
    
    def add_fishes(self, fishes: list[int]) -> None:
        for n in fishes:
            self.fishes[n] += 1

    def on_day(self, day: int) -> int:
        for i in range(self.day, day):
            self.fishes[(i+7)%9] += self.fishes[i % 9]
        self.day += i
        return sum(self.fishes)

all_fish = Fishes()
all_fish.on_day(18)
all_fish.on_day(80)
all_fish.on_day(256)
