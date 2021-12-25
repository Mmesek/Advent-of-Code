from AoC.utils import get_input


def prepare_boards() -> tuple[list[int], list[list[int]]]:
    """Retrieves order and boards from puzzle input"""
    puzzle_input = get_input(4, lambda x: [int(n) for n in x.replace(",", " ").split(" ") if n])
    boards = []
    board = []
    for i in puzzle_input:
        if not i:
            if board:
                boards.append(board)
            board = []
        if i:
            board.append(i)
    boards.append(board)
    order = boards[0][0]
    boards = boards[1:]
    return order, boards


def sum_unmarked(board: list[list[int]], marked: list[int]) -> int:
    """Summarizes not marked numbers"""
    unmarked = []
    for row in board:
        for n in row:
            if n not in marked:
                unmarked.append(n)
    return sum(unmarked)


def find_winning_boards() -> int:
    """Generator yielding winning boards in order"""
    discarded_boards = []
    for x, i in enumerate(order):
        previous_numbers = order[:x] + [i]
        for _x, board in enumerate(boards):
            if _x in discarded_boards:
                continue
            for column, row in enumerate(board):
                if all(n in previous_numbers for n in row) or all(
                    n in previous_numbers for n in [_r[column] for _r in board]
                ):
                    u = sum_unmarked(board, previous_numbers)
                    print(u, i)
                    yield u * i
                    discarded_boards.append(_x)
                    break


order, boards = prepare_boards()
print([score for score in find_winning_boards()])
