from AoC.utils import get_input

rules = get_input(7)

def check_rules(search_bags):
    _bags = []
    for rule in rules:
        bags = rule.split('contain')
        if any(bag in bags[1] for bag in search_bags):
            _bags.append(bags[0].strip().replace('bags', 'bag'))
    return _bags

search_bags = ['shiny gold bag']
total_bags = []
for i in range(len(rules)):
    search_bags = check_rules(search_bags)
    total_bags += search_bags
print(len(set(total_bags)))

def get_bags(rules):
    bags = {}
    for line in rules:
        _bag = line.split(' contain ')
        if 'no other bag' not in _bag[1]:
            bags[_bag[0].replace('bags', 'bag')] = [[j for j in i.strip().strip('.').replace('bags','bag').split(' ',1)] for i in _bag[1].split(',')]
    return bags

bags = get_bags(rules)

def get(bag):
    c = 1
    if bag in bags:
        for amount, inner in bags[bag]:
            c += int(amount) * get(inner)
    return c

print(get('shiny gold bag')-1)
