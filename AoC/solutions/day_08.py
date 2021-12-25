signals = [[[s for s in signal.split(" ") if s] for signal in i.split("|") if signal] for i in """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".splitlines() if i]
from AoC.utils import get_input
signals = get_input(8, lambda x: [[s for s in signal.split(" ") if s] for signal in x.split("|") if signal])

#######
#  0  #
# 1 2 #
#  3  #
# 4 5 #
#  6  #
#######

positions = {
    0: [0,1,2,4,5,6],
    1: [2,5],
    2: [0,2,3,4,6],
    3: [0,2,3,5,6],
    4: [1,2,3,4],
    5: [0,1,3,5,6],
    6: [0,1,3,4,5,6],
    7: [0,2,5],
    8: [0,1,2,3,4,5,6],
    9: [0,1,2,3,5,6]
}

mapped_positions = {k:[] for k in range(7)}
rev_positions = {k:[] for k in range(10)}

for k,v in positions.items():
    for pos in v:
        mapped_positions[pos].append(k)
        rev_positions[k].append(pos)

pos_to_num = mapped_positions
num_to_pos = rev_positions

print(mapped_positions)
print(rev_positions)

unique_positions = {}
for k,v in positions.items():
    if len(v) not in unique_positions.keys():
        unique_positions[len(v)] = k
    else:
        unique_positions[len(v)] = 0

alpha_to_num = {k:v for v, k in enumerate("abcdefg")}

def digit_from_positions(mapping: dict[int, list[int]], value: str):
    digit = set()
    for position in value:
        position = alpha_to_num[position]
        p = list(filter(lambda x: position in mapping[x], mapping))
        #digit.append(p)
        #digit.append(mapping[position])
    return next(filter(lambda x: mapping[x] == sorted(list(digit)), mapping), None)

print(digit_from_positions(pos_to_num, "acf"))

def analyse(signal_patterns: list[str]) -> dict[int, list[int]]:
    """Analyses pattern and returns mapping"""
    guessed_positions = {k:[] for k in range(10)}
    # Number corresponding to required fields to be lit
    for pattern in signal_patterns:
        pass
    return guessed_positions

def retrieve_code(output_values: list[str], mapping: dict[int, list[int]]):
    code = []
    for value in output_values:
        code.append(digit_from_positions(mapping, value))


code = []
i = 0
for signal, output in signals:
    for value in output:
        lit = [i for i in range(7)]
        for pos in value:
            as_num = alpha_to_num[pos]
            new = []
            values = mapped_positions[as_num]
            for v in values:
                if v in lit:
                    new.append(v)
            lit = new
        possible_code = []
        for digit, _positions in positions.items():
            if all(i in _positions for i in lit):
                possible_code.append(digit)
            if len(lit) == len(_positions):
                i += 1
                break
        code.append(possible_code)
        
#        if unique_positions.get(len(value)):
#            i += 1
#print(code)

i = 0
for signal, output in signals:
    for value in output:
        if len(value) in {2,4,3,7}:
            i+= 1
print(i)

