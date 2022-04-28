# -*- coding: utf8 -*-
import sys
from collections import deque, namedtuple
from os import system

BLANK = "O"
BOARD = []

class Board:
    def __init__(self, w, h, value=BLANK):
        """Create a array - 'I' Command."""
        self.board = [[value] * w for _ in range(h)]

    def __str__(self):
        """Print the Board"""
        return '\n'.join(("".join(row) for row in self.board))

    @property
    def width(self):
        return len(self.board[0])

    @property
    def height(self):
        return len(self.board)

    @staticmethod
    def _index(self, coord):
        return coord - (1,1)

    def __getitem__(self, coord):
        c = self._index(coord)
        return self.board[c.y][c.x]

    def __setitem__(self, coord, value):
        self.board[y(coord) - 1][x(coord) - 1] = value

    def set_many(self, coords, value):
        for c in coords:
            self[c] = value

    def items(self):
        for coord in coords_of(self):
            yield coord, self[coord]

    def get_many(self, coords):
        for coord in coords:
            yield self[coord]

    def __contains__(self, coord):
        """Check if a cmd is out of list range."""
        return 1 <= x(coord) <= self.width and 1 <= y(coord) <= self.height

class Coord(namedtuple('Coord', 'x y')):
    def __add__(self, other):
        return Coord(self.x + other[0], self.y + other[1])

def x(c):
    return c[0]

def y(c):
    return c[1]

def get_board():
    return BOARD

#def offset(coord, rel):
#    ''' Calcula o deslocamento de uma dada coordenada.'''
#    return x(coord) + x(rel), y(coord) + y(rel)

def region(col_start, row_start, col_end, row_end):
    for row in range(row_start, row_end + 1):
        for col in range(col_start, col_end + 1):
            yield Coord(col, row)

def coords_of(board):
    yield from region(1, 1, board.width, board.height)



#def flood(coord, inside, key, strategy=((-1,0), (1,0), (0,-1), (0, 1))):
#    if not inside(coord):
#        return
#
#    yield coord
#
#    neighbor = (offset(coord, rel) for rel in strategy)
#
#    for n in neighbor:
#        if inside(n) and key(n):
#                yield from flood(n, inside, key)

def flood(original, inside, key, strategy=((-1,0), (1,0), (0,-1), (0, 1))):
    visited = set()
    pending = deque((original,))

    while pending:
        coord = pending.pop()
        visited.add(coord)

        yield coord

        neighbors = (offset(coord, rel) for rel in strategy)

        for n in neighbors:
            if (n not in visited
                    and inside(n)
                    and key(n)):
                pending.append(n)

'''
def color_pixel(board, col, row, color):
    """ Change the color of one pixel - 'L' Command. """
    set_item(board, (col, row), color)


def ver_pixel(board, col, row_start, row_end, color):
    """Change the color of a column - 'V' Command."""
    set_many(board, region(col, row_start, col, row_end), color)


def hor_pixel(board, col_start, col_end, row, color):
    """Change the color of a line - 'H' Command."""
    set_many(board, region(col_start, row, col_end, row), color)


def block_pixel(board, col_start, row_start, col_end, row_end, color):
    """Change color of an entire block - 'K' Command."""
    set_many(board, region(col_start, row_start, col_end, row_end), color)


def fill_pixel(board, col, row , new_color):
    """ Fill a continuous region 'F' command."""
    coord = (col, row)

    old_color = get_item(board, coord)

    def bound(coord):
        return contains(board, coord)

    def same_color(neighbor):
        return get_item(board, neighbor) == old_color

    set_many(board, flood(coord, inside=bound, key=same_color), new_color)
'''
def save_array(board, filename):
    """ Save the array with the 'S' command. """
    with open(filename, "w") as f:
        f.write(string(board))

def prompt(convert):
    while True:
        value = input('> ')
        value = value.strip()

        try:
            value = convert(value)
        except ValueError as e:
            print(e)
        else:
            break

    return value

def parse(text, options='ICLVHKFSX'):
    """Parse and validate a command string."""
    tokens = text.upper().split()

    if not tokens or tokens[0] not in options:
        raise ValueError('Comando inválido.')

    for i, t in enumerate(tokens):
        if t.isdigit():
            tokens[i] = int(t)

    return tokens

def invoke(board, tokens):
    commands = {
        'X': sys.exit,
        'I': create,
        'L': color_pixel,
        'V': ver_pixel,
        'H': hor_pixel,
        'K': block_pixel,
        'F': fill_pixel,
        'S': save_array,
        'C': clear,
    }

    cmd, *args = tokens
    f = commands[cmd]
    f(board, *args)

def main():
    board = []

    while True:
        try:
            system('clear')
            print(string(board))
            cmd = prompt(parse)
            invoke(board, cmd)

        except TypeError:
            print('Argumentos inválidos.')

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()