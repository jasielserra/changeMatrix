from copy import deepcopy
from os import system
from time import sleep
from gameoflife.bitmap import Board

DEAD = chr(0x00B7)
LIVE = chr(0x2588)

SURROUDING = tuple((a,b)
                   for a in range(-1,2)
                   for b in range(-1,2)
                   if not (a == b == 0))

GLIDER = ((2,1), (3,2), (1,3), (2,3), (3,3))

def neighbors(c):
    yield from (c + rel for rel in SURROUDING)
    #yield from ((x(c) + a, y(c) + b) for a, b in SURROUDING)

def wrap(c, w, h):
    yield from ((a % w, b % h) for a,b in c)

def should_die(total):
    return total < 2 or total > 3

def should_ressurect(total):
    return total == 3

def rule(c, status, total):
    s = status
    if status == LIVE:
        if should_die(total):
            s = DEAD
    else:
        if should_ressurect(total):
            s = LIVE
    return s

def how_many_alive(l):
    return sum(1 for s in l if s == LIVE)

def setup():
    board = Board(50, 25, DEAD)
    board.set_many(GLIDER, LIVE)
    return board

def update(board):
    new_board = deepcopy(board)
    for coord, status in board.items():
        n = neighbors(coord)
        n = wrap(n, board.width, board.height)
        ns = board.get_many(n)
        total = how_many_alive(ns)

        new_board[coord] = rule(coord, status, total)

    return new_board

def show(board):
    system('clear')
    print(board)


def main():
    board = setup()

    while True:
        try:
            board = update(board)
            show(board)
            sleep(0.05)
        except (KeyboardInterrupt, SystemExit):
            break


if __name__ == '__main__':
    main()