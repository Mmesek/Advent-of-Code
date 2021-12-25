from AoC.utils import get_input

notes = get_input(19)

rules = []
messages = []

for x, line in enumerate(notes):
    if line == '':
        break
    rules.append(line)

for line in notes[x+1:]:
    messages.append(line)

compiled_rules = {}
for rule in rules:
    number, rule = rule.split(': ')
    values=[]
    for j in rule.split('|'):
        _values = []
        for i in j.split(' '):
            if i.strip().isdigit():
                _values.append(int(i.strip()))
            elif i.strip() == "":
                continue
            else:
                _values.append(i.strip('"'))
        values.append(_values)
    compiled_rules[int(number)] = values

def get_value(rule):
    _rule = compiled_rules[rule]
    for sub_rule in _rule:
        for number in sub_rule:
            if type(number) == int:
                return get_value(number)
            else:
                return number

_compiled_rules = {}
def compile_rules():
    for rule in compiled_rules:
        _rule = []
        for group in compiled_rules[rule]:
            _group = []
            for sub in group:
                if type(sub) == int:
                    _group.append(get_value(sub))
                else:
                    _group.append(sub)
            _rule.append(_group)
        _compiled_rules[rule] = _rule
    return _compiled_rules
_compiled_rules = compile_rules()
get_value(3)

        


print(1)