from copy import deepcopy
from os import system
from time import sleep

from matriz import create_array, set_many, string, offset, coords_of, get_item, set_item, items, get_many

DEAD = chr(0x00B7)
LIVE = chr(0x2588)

WIDTH, HEIGHT = 50, 25

GLIDER = ((2,1), (3,2), (1,3), (2,3), (3,3))

SURROUDING = tuple((a,b)
                   for a in range(-1,2)
                   for b in range(-1,2)
                   if not (a == b == 0))


def neighbors(c):
    yield from ((x(c) + a, y(c) + b) for a, b in SURROUDING)

def wrap(c, w, h):
    yield from ((a % w, b % h for a,b in c))

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

def main():

    board = []
    create(board, 50, 25)
    clear(board, DEAD)
    set_many(board, GLIDER, LIVE)

    while True:
        try:
            system('clear')
            print(string(board))

            new_board = deepcopy(board)
            for coord, status in items(board):
                n = neighbors(coord)
                n = wrap(n, width(board), height(board))
                ns = get_many(board, n)
                total = how_many_alive(ns)

                set_item(new_board, coord, rule(coord, status, total))

            board = new_board
            sleep(0.05)
        except (KeyboardInterrupt, SystemExit):
            break


if __name__ == '__main__':
    main()