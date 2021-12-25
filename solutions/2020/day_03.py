from AoC.utils import get_input
trees = get_input(3, lambda i: i * 323)

def check_slope(slope, skip=1):
    _trees = []
    for x, tree in enumerate(trees):
        if skip != 1 and x % skip == 0:
            continue
        if '#' == tree[x*slope]:
            _trees.append(tree[x*slope])
    print('Slope', slope, skip, ':', len(_trees))
    return len(_trees)

print(check_slope(3))
print(check_slope(1) * check_slope(3) * check_slope(5)*check_slope(7)* check_slope(1, 2))