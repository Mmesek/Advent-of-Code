from AoC.utils import get_input
signals = get_input(8, lambda x: [[s for s in signal.split(" ") if s] for signal in x.split("|") if signal])

i = 0
for signal, output in signals:
    for value in output:
        if len(value) in {2,4,3,7}:
            i+= 1

print(i)
