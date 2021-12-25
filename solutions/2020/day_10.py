from AoC.utils import get_input

jolts = sorted(get_input(10, lambda i: int(i)) + [0])
counter = {0:1}
d1, d3 = 0, 0

for x, jolt in enumerate(jolts):
    if jolt-jolts[x-1] == 1:
        d1 += 1
    elif jolt-jolts[x-1] == 3:
        d3 += 1

    for i in range(1,4):
        if jolt+i not in jolts:
            continue
        if jolt+i not in counter:
            counter[jolt+i] = 0
        counter[jolt+i] += counter[jolt]

print(d1*(d3+1))
print(counter[jolts[-1]])
