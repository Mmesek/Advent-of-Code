from AoC.utils import get_input
instructions = get_input(12, lambda i: (i[0], int(i[1:])))

class Waypoint:
    def __init__(self):
        self.x = 10
        self.y = 1
    def forward(self, value):
        return self.x * value, self.y * value
    def rotate(self, value):
        v = (value // 90)
        for i in range(abs(v)):
            if v > 0:
                self.x, self.y = self.y, -self.x
            else:
                self.x, self.y = -self.y, self.x

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, x, y):
        self.x += x
        self.y += y

ship = Ship()
waypoint = Waypoint()
for action, value in instructions:
    if action == 'R':
        waypoint.rotate(value)
    elif action == 'L':
        waypoint.rotate(-value)
    elif action == 'F':
        ship.move(*waypoint.forward(value))

    elif action == 'N':
        waypoint.y += value
    elif action == 'S':
        waypoint.y -= value
    elif action == 'E':
        waypoint.x += value
    elif action == 'W':
        waypoint.x -= value

print(abs(ship.x) + abs(ship.y))
