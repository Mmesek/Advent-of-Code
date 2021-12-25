from AoC.utils import get_input
seats = get_input(11, lambda i: [j for j in i])

def check_seat(x, y):
    if seats[y][x] == '#':
        return 1
    return 0

def check_left(x, y):
    if x - 1 >= 0:
        return check_seat(x-1, y)
    return 0

def check_right(x, y):
    if x + 1 < len(seats[y]):
        return check_seat(x+1, y)
    return 0

def check_upper(x, y):
    upper = 0
    if y - 1 >= 0:
        upper += check_seat(x, y-1)
        upper += check_left(x, y-1)
        upper += check_right(x, y-1)
    return upper

def check_below(x, y):
    below = 0
    if y + 1 < len(seats):
        below += check_seat(x, y+1)
        below += check_left(x, y+1)
        below += check_right(x, y+1)
    return below

def check_adjacent(x, y):
    occupied = 0
    occupied += check_left(x, y)
    occupied += check_right(x, y)
    occupied += check_upper(x, y)
    occupied += check_below(x, y)
    return occupied

def _round(seats, copy):
    for y, row in enumerate(seats):
        for x, seat in enumerate(row):
            if seat == '.':
                continue
            adjacent_occupied = check_adjacent(x, y)
            if adjacent_occupied == 0:
                copy[y][x] = '#'
            elif adjacent_occupied >= 4:
                copy[y][x] = 'L'
    return copy

from copy import deepcopy
def do_round():
    x= 0
    while True:
        x+=1
        global seats
        copy = deepcopy(seats)
        copy = _round(seats, copy)
        if seats == copy:
            return copy, x
        seats = deepcopy(copy)
        
def calc_occupied(seats):
    occupied = 0
    for y, row in enumerate(seats):
        occupied += seats[y].count('#')
    return occupied

_seats, rounds = do_round()
print(calc_occupied(_seats),'in',rounds,'rounds')
