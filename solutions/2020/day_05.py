from AoC.utils import get_input
passes = get_input(5)

def binary_search(lower, upper, upper_half=False):
    mid = (upper + lower) // 2
    if not upper_half:
        #Lower half
        return [lower, mid-1]
    else:
        #Upper half
        return [mid+1, upper]

decoded = []

for bp in passes:
    row = [0, 127]
    column = [0, 7]
    for char in bp:
        if char == 'F':
            row = binary_search(row[0], row[1])
        elif char == 'B':
            row = binary_search(row[0], row[1], True)
        elif char == 'L':
            column = binary_search(column[0], column[1])
        elif char == 'R':
            column = binary_search(column[0], column[1], True)
    decoded.append(row[0] * 8 + column[0])

_decoded = sorted(decoded, reverse=True)
print(_decoded[0])

_previous = _decoded[0]
for i in _decoded:
    if i - _previous < -1:
        print(i+1)
    _previous = i