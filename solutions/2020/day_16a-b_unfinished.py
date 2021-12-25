from AoC.utils import get_input

notes = get_input(16)
fields = {}
ticket = []
tickets = []
for x, note in enumerate(notes):
    if 'your ticket' in note:
        ticket = [int(i) for i in notes[x+1].split(',')]
        continue
    elif 'nearby tickets' in note:
        tickets = [[int(i) for i in _ticket.split(',')] for _ticket in notes[x+1:]]
        continue
    elif ':' in note:
        field, value = note.split(':')
        fields[field] = [[int(j) for j in i.split('-')] for i in value.strip().split(' or ')]
invalid = []
valid_tickets = []
for _ticket in tickets:
    invalid_ticket = False
    for field in _ticket:
        valid = False
        for _field in fields:
            if (field >= fields[_field][0][0] and field <= fields[_field][0][1] or field >= fields[_field][1][0] and field <= fields[_field][1][1]):
                valid = True
        if not valid:
            invalid.append(field)
            invalid_ticket = True
    if not invalid_ticket:
        valid_tickets.append(_ticket)

print("Part 1:", sum(invalid))

matched = []
departure = []
for x, number in enumerate(ticket):
    total_matching = [i for i in fields]#.difference(matched)
    for _field_name in fields:
        _field = fields[_field_name]
        ticket_not_matching = []#set()
        for _ticket in valid_tickets:
            _ticket = _ticket[x]
            if not (_ticket >= _field[0][0] and _ticket <= _field[0][1]) and not (_ticket >= _field[1][0] and _ticket <= _field[1][1]):
                #if _field_name in total_matching:
                ticket_not_matching.append(_field_name)#add(_field_name)
        #if len(ticket_not_matching) > 0:
        total_matching = [i for i in total_matching if i not in ticket_not_matching]#total_matching.intersection(ticket_matching)
    matched += list(total_matching)
    print(total_matching, number)
    if 'departure' in list(total_matching)[0]:
        departure.append(number)

print(departure)