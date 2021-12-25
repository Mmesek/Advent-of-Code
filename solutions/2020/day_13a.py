from AoC.utils import get_input

notes = get_input(13)

timestamp = int(notes[0])
buses = [int(i) for i in filter(lambda i: i != 'x', notes[1].split(','))]

departures = []
for bus in buses:
    t = 0
    while True:
        t += bus
        if t > timestamp:
            departures.append((t, bus))
            break
departures = sorted(departures, key=lambda i: i[0])
print((departures[0][0] - timestamp) * departures[0][1])
