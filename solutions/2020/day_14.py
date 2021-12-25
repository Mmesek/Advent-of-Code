from AoC.utils import get_input
import itertools

instructions = get_input(14, lambda i: i.split(' = '))

mem_p1 = {}
mem = {}

def unmask(mask, new_value, address, not_a):
    if len(address) != len(mask):
        address = '0'*(len(mask) - len(address)) + address
    for x, v in enumerate(mask):
        if v != not_a:
            new_value.append(v)
        else:
            new_value.append(address[x])
    return new_value

for instruction, value in instructions:
    if instruction == 'mask':
        mask = value
    else:
        new_value = []
        address = int(instruction.split('[')[1].replace(']',''))
        address = bin(int(address))[2:]
        mem_p1[address] = int(''.join(unmask(mask, [], bin(int(value))[2:], "X")), 2)
        unmask(mask, new_value, address, "0")
        floats = []
        for i in range(new_value.count('X')):
            floats.append('0')
            floats.append('1')
        for binary in itertools.combinations(floats, new_value.count('X')):
            _new_value = new_value.copy()
            _x = 0
            for x, char in enumerate(_new_value):
                if char == 'X':
                    _new_value[x] = binary[_x]
                    _x += 1
            _new_value = ''.join(_new_value)
            mem[int(_new_value, 2)] = int(value)

print(sum(mem_p1.values()))
print(sum(mem.values()))
