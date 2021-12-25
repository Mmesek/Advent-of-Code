from AoC.utils import get_input
instructions = get_input(12, lambda i: (i[0], int(i[1:])))

directions = ['E', 'S', 'W', 'N']
current_direction = 0
positions = [0,0]
for action, value in instructions:
    if action == 'R':
        current_direction += value // 90
    elif action == 'L':
        current_direction -= value // 90
    elif action == 'F':
        action = directions[current_direction % 4]

    if action == 'N':
        positions[0] += value
    elif action == 'S':
        positions[0] -= value
    elif action == 'W':
        positions[1] += value
    elif action == 'E':
        positions[1] -= value

print(abs(positions[0]) + abs(positions[1]))