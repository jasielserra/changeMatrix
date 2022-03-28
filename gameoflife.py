from copy import deepcopy
from os import system
from matriz import create_array, set_many, string, offset, coords_of, get_item

DEAD = chr(0x00B7)
LIVE = chr(0x2588)

GLIDER = ((2,1), (3,2), (1,3), (2,3), (3,3))

SURROUDING = tuple((a,b)
                   for a in range(-1,2)
                   for b in range(-1,2)
                   if not (a == b == 0))

def main():
    def neighbors(c):
        yield from (offset(c,r) for r in SURROUDING)

    board = []
    create_array(board, 50, 25, DEAD)
    set_many(board, GLIDER, LIVE)


    system('clear')
    print(string(board))

    new_board = deepcopy(board)
    for coord in coords_of(board):
        status = get_item(board, coord)




if __name__ == '__main__':
    main()