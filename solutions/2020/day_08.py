from AoC.utils import get_input
instructions = get_input(8, lambda i: (i.split(' ')[0], int(i.split(' ')[1])))

def run(instructions):
    accumulator = 0
    _visited = []
    x = 0
    while True:
        if x < len(instructions):
            operation, argument = instructions[x]
        else:
            break
            
        if x in _visited:
            return (False, accumulator)

        _visited.append(x)

        if operation == 'jmp':
            x += argument
        else:
            x += 1
        if operation == 'acc':
            accumulator += argument
    return accumulator

for x, op in enumerate(instructions):
    copy = instructions.copy()
    if op[0] == 'jmp':
        copy[x] = ('nop', op[1])
    elif op[0] == 'nop':
        copy[x] = ('jmp', op[1])
    else:
        continue
    result = run(copy)
    if type(result) is int or result[0] is not False:
        break

print(run(instructions))
print('TERMINATED', result)