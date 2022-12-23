from AoC.utils import solve


example = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".splitlines()


def parse(puzzle_input: list[str]) -> dict:
    sensors = []
    beacons = set()
    for sensor, beacon in puzzle_input:
        sensor = sensor.split("=")
        sensor_x, sensor_y = int(sensor[-2].split(",")[0]), int(sensor[-1])

        beacon = beacon.split("=")
        beacon_x, beacon_y = int(beacon[-2].split(",")[0]), int(beacon[-1])

        sensors.append((sensor_x, sensor_y, (abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y))))

        beacons.add((beacon_x, beacon_y))
        beacons.add((sensor_x, sensor_y))

    return sensors, beacons


def solution(puzzle_input: list[str], y: int = 10) -> int:
    taken = set()
    sensors, beacons = parse(puzzle_input)

    for _x, _y, distance in sensors:
        for x in range(_x - distance, _x + distance + 1):
            if (abs(_x - x) + abs(_y - y)) <= distance and (x, y) not in beacons:
                taken.add(x)

    return len(taken)


def solution_2(puzzle_input: list[str]) -> int:
    sensors, _ = parse(puzzle_input)
    x = 0
    for y in range(4000000):
        current_end = 0
        ranges = []

        for _x, _y, distance in sensors:
            if (dy := abs(_y - y)) <= distance:
                ranges.append((_x - (distance - dy), _x + (distance - dy)))

        for start, end in sorted(ranges):
            if start > current_end:
                x = start - 1
                break
            current_end = max(end, current_end)

        if x:
            break

    return x * 4000000 + y


solve(15, 1, solution, lambda x: x.split(":"), example, 0, y=2000000)
solve(15, 2, solution_2, lambda x: x.split(":"), example, 56000011)
