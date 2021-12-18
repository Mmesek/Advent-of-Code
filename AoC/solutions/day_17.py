from AoC.utils import get_input

area = get_input(17, lambda x: x.split(" "))[0]

for i in area[2:]:
    if "x=" or "y=" in i:
        axis, coords = i.split("=")
        if axis == "x":
            x_min, x_max = [int(i) for i in coords.replace(",", "").split("..")]
        else:
            y_min, y_max = [int(i) for i in coords.replace(",", "").split("..")]


def shoot_probe(initial_x: int, initial_y: int) -> list[int]:
    x = 0
    y = 0
    highest_point = 0

    x_velocity = initial_x
    y_velocity = initial_y
    while True:
        x += x_velocity
        y += y_velocity
        if x_velocity > 0:
            x_velocity -= 1
        y_velocity -= 1
        if y > highest_point:
            highest_point = y
        if x in range(x_min, x_max + 1) and y in range(y_min, y_max + 1):
            return initial_x, initial_y, highest_point
        if y < y_min:
            break


def solve():
    success_velocity = []
    for x in range(x_max + 1):
        for y in range(-250, 250):
            hit = shoot_probe(x, y)
            if hit:
                success_velocity.append(hit)
    return success_velocity


velocities = solve()
print(sorted(velocities, key=lambda x: x[-1], reverse=True)[0])
print(len(velocities))
