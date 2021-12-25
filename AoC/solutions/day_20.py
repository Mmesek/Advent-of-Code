example = [i for i in """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###""".splitlines() if i]

def enhance(image: list[list[str]], algorithm: str):
    import copy
    new_image = copy.deepcopy(image)
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            pos = find_pixel(x, y, image)
            new_image[y][x] = algorithm[pos]
    return new_image

def find_pixel(x: int, y: int, image: list[list[str]]):
    binary = ""
    if y:
        if x:
            binary += image[y-1][x-1]
        else:
            binary += "."
        binary += image[y-1][x]
        if x < len(image[y-1]) - 1:
            binary += image[y-1][x+1]
        else:
            binary += "."
    else:
        binary += "..."

    if x:
        binary += image[y][x-1]
    else:
        binary += "."
    binary += image[y][x]
    if x < len(image[y]) - 1:
        binary += image[y][x+1]
    else:
        binary += "."

    if y < len(image) - 1:
        if x:
            binary += image[y+1][x-1]
        else:
            binary += "."
        binary += image[y+1][x]
        if x < len(image[y+1]) - 1:
            binary += image[y+1][x+1]
        else:
            binary += "."
    else:
        binary += "..."

    t = binary.maketrans({".":"0", "#":"1"})
    pos = int(binary.translate(t), base=2)
    return pos

def resize_image(image: list[list[str]]):
    wrapper = list("." * (len(image[0]) + 2))
    new_image = [wrapper]
    for line in image:
        nline = line.copy()
        nline.insert(0, ".")
        nline.append(".")
        new_image += [nline]
    new_image += [wrapper]
    return new_image

def show(image: list[list[str]]):
    for i in image:
        print("".join(i))
    print()

from AoC.utils import get_input
text = example
#text = get_input(20, lambda x: [i for i in x if i])
algorithm, image = text[0], [list(i) for i in text[2:]]
print(len(algorithm))
#print(find_pixel(2,2, image) == 34)

#show(image)

for i in range(2):
    print("Enhancing...")
    image = resize_image(image)
    image = resize_image(image)
    image = enhance(image, algorithm)

show(image)
print(sum([i.count("#") for i in image]))
