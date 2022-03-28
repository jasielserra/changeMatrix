from copy import deepcopy
from os import system
from time import sleep

from matriz import create_array, set_many, string, offset, coords_of, get_item, set_item

DEAD = chr(0x00B7)
LIVE = chr(0x2588)

GLIDER = ((2,1), (3,2), (1,3), (2,3), (3,3))

SURROUDING = tuple((a,b)
                   for a in range(-1,2)
                   for b in range(-1,2)
                   if not (a == b == 0))


def neighbors(c):
    yield from (offset(c, r) for r in SURROUDING)

def wrap(c,w, h):
    yield from ((a % w, b % h) for a,b in c)

def main():

    board = []
    create_array(board, 50, 25, DEAD)
    set_many(board, GLIDER, LIVE)


    system('clear')
    print(string(board))

    new_board = deepcopy(board)
    for coord in coords_of(board):
        status = get_item(board, coord)

        total = 0
        for n in neighbors(coord):
            ns = get_item(board, n)
            if ns == LIVE:
                total += 1

        s = status = get_item(board, coord)
        if status == LIVE:
            if total < 2 or total > 3:
                s = DEAD
            else:
                if total == 3:
                    s = LIVE

            set_item(new_board, coord, s)

        board = new_board
        sleep(0.05)






if __name__ == '__main__':
    main()