import re
from AoC.utils import get_input


class Dice:
    def __init__(self) -> None:
        self.i = 0
        self.rolls = 0

    def roll(self) -> int:
        self.i += 1
        if self.i > 100:
            self.i = 1
        self.rolls += 1
        return self.i


def starting_positions(positions: list[str]) -> dict[str, int]:
    regex = re.compile(r"Player (\d+) starting position: (\d+)")
    players = {}
    for line in positions:
        r = regex.match(line)
        g = r.groups()
        player, position = g
        players[player] = int(position)
    return players


def play(score: int) -> int:
    dice = Dice()
    while True:
        for player in players:
            rolls = []
            for i in range(3):
                rolls.append(dice.roll())

            p = (players[player] + sum(rolls)) % 10
            if p == 0:
                p = 10
            players[player] = p
            scores[player] += players[player]
            if scores[player] >= score:
                return dice.rolls


players = starting_positions(get_input(21))
scores = {k: 0 for k in players.keys()}

print(play(1000) * min(scores.values()))
