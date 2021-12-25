from AoC.utils import get_input
instructions = get_input(12, lambda i: (i[0], int(i[1:])))

ship = [0,0]
waypoint = [10,1]

for action, value in instructions:
    if action in 'RL':
        if action == 'L':
            value = -value
        v = (value // 90)
        for i in range(abs(v)):
            if v > 0:
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
            else:
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    elif action == 'F':
        ship[0] += waypoint[0] * value
        ship[1] += waypoint[1] * value

    elif action == 'N':
        waypoint[1] += value
    elif action == 'S':
        waypoint[1] -= value
    elif action == 'E':
        waypoint[0] += value
    elif action == 'W':
        waypoint[0] -= value

print(abs(ship[0]) + abs(ship[1]))
