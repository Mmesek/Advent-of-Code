from AoC.utils import get_input
seats = get_input(11, lambda i: [j for j in i])

from enum import Enum

class Directions(Enum):
    Left = 0
    Right = 1
    Up = 2
    UpperLeft = 3
    UpperRight = 4
    Down = 5
    BottomLeft = 6
    BottomRight = 7

def check_seat(x, y, direction):
    if direction is Directions.Left:
        if x - 1 >= 0:
            x = x-1
        else:
            return 0
    elif direction is Directions.Right:
        if x + 1 < len(seats[y]):
            x = x+1
        else:
            return 0
    elif direction is Directions.Up:
        if y + 1 < len(seats):
            y = y+1
        else:
            return 0
    elif direction is Directions.Down:
        if y - 1 >= 0:
            y = y-1
        else:
            return 0
    elif direction is Directions.UpperLeft:
        if y - 1 >= 0 and x - 1 >= 0:
            x = x-1 
            y = y-1
        else:
            return 0
    elif direction is Directions.UpperRight:
        if y - 1 >= 0 and x + 1 < len(seats[y]):
            x = x+1 
            y = y-1
        else:
            return 0
    elif direction is Directions.BottomLeft:
        if y + 1 < len(seats) and x - 1 >= 0:
            x = x-1
            y = y+1
        else:
            return 0
    elif direction is Directions.BottomRight:
        if y + 1 < len(seats) and x + 1 < len(seats[y]):
            x = x+1
            y = y+1
        else:
            return 0
    if seats[y][x] == '#':
        return 1
    elif seats[y][x] == '.':
        return check_seat(x, y, direction)
    return 0

def check_adjacent(x, y):
    occupied = 0
    occupied += check_seat(x, y, Directions.Left)
    occupied += check_seat(x, y, Directions.Right)
    occupied += check_seat(x, y, Directions.Up)
    occupied += check_seat(x, y, Directions.UpperLeft)
    occupied += check_seat(x, y, Directions.UpperRight)
    occupied += check_seat(x, y, Directions.Down)
    occupied += check_seat(x, y, Directions.BottomLeft)
    occupied += check_seat(x, y, Directions.BottomRight)
    return occupied


def _round(seats, copy):
    for y, row in enumerate(seats):
        for x, seat in enumerate(row):
            if seat == '.':
                continue
            adjacent_occupied = check_adjacent(x, y)
            if adjacent_occupied == 0:
                copy[y][x] = '#'
            elif adjacent_occupied >= 5:
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
