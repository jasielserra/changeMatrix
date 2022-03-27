# -*- coding: utf8 -*-
from collections import deque

BLANK = "O"

def width(board):
    return len(board[0])

def height(board):
    return len(board)

def x(coord):
    return coord[0]

def y(coord):
    return coord[1]

def offset(coord, rel):
    return x(coord) + x(rel), y(coord) + y(rel)

def set_item(board, coord, value):
    board[y(coord) - 1][x(coord) - 1] = value

def get_item(board, coord):
    return board[y(coord) - 1][x(coord) - 1]

def region(col_start, row_start, col_end, row_end):
    for row in range(row_start, row_end + 1):
        for col in range(col_start, col_end + 1):
            yield col, row

def contains(board, coord):
    """Check if a cmd is out of list range."""
    return 1 <= x(coord) <= width(board) and 1 <= y(coord) <= height(board)

def flood(coord, inside, key, strategy=((-1,0), (1,0), (0,-1), (0, 1))):
    if not inside(coord):
        return

    yield coord

    neighbor = (offset(coord, rel) for rel in strategy)

    for n in neighbor:
        if inside(n) and key(n):
                yield from flood(n, inside, key)

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


def set_many(board, coords, value):
    for c in coords:
        set_item(board, c, value)

def coords_of(board):
    yield from region(1, 1, width(board), height(board))


def read_sequence():
    """
    Read and validate a sequence of commands.
    """
    charValid = ("ICLVHKFSX")
    sqc = input("Digite um comando: ").upper()
    sqc = sqc.split()

    for char in charValid:
        if char == sqc[0] and not "":
            return sqc
    else:
        print("\nComando Inválido!\n")
        return sqc


def create_array(w, h, value=BLANK):
    """Create a array - 'I' Command."""
    return [[value] * w for _ in range(h)]


def clean_array(board, value=BLANK):
    """ Clean a array - 'C' Command."""
    # TODO: range conhece muito sobre a estrutura do board.
    set_many(board, coords_of(board), value)
    return board


def color_pixel(board, coord, color):
    """ Change the color of one pixel - 'L' Command. """
    set_item(board, coord, color)
    return board


def ver_pixel(board, col, row_start, row_end, color):
    """Change the color of a column - 'V' Command."""
    set_many(board, region(col, row_start, col, row_end), color)
    return board


def hor_pixel(board, col_start, col_end, row, color):
    """Change the color of a line - 'H' Command."""
    set_many(board, region(col_start, row, col_end, row), color)
    return board


def block_pixel(board, col_start, row_start, col_end, row_end, color):
    """Change color of an entire block - 'K' Command."""
    set_many(board, region(col_start, row_start, col_end, row_end), color)
    return board

def fill_pixel(board, coord, new_color):
    """ Fill a continuous region 'F' command."""

    old_color = get_item(board, coord)

    def bound(coord):
        return contains(board, coord)

    def same_color(neighbor):
        return get_item(board, neighbor) == old_color

    set_many(board, flood(coord, inside=bound, key=same_color), new_color)

    return board


def save_array(board, filename):
    """ Save the array with the 'S' command. """
    with open(filename, "w") as f:
        f.write(string(board))


def string(board):
    return '\n'.join(("".join(row) for row in board))

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
    '''Parse and validate a command string.'''
    tokens = text.upper().split()

    if not tokens or tokens[0] not in options:
        raise ValueError('Comando inválido.')

    for i, t in enumerate(tokens):
        if t.isdigit():
            tokens[i] = int(t)

    return tokens

def main():
    while True:
        try:
            print(string(board))

            cmd, *args = prompt(parse)
            if cmd == "X":
                break

            elif cmd == "I":
                board = create_array(int(cmd[0]), int(cmd[1]))

            elif cmd == "L":
                board = color_pixel(board, *args)

            elif cmd == "V":
                board = ver_pixel(board, *args)

            elif cmd == "H":
                board = hor_pixel(board, *args)

            elif cmd == "K":
                board = block_pixel(board, *args)

            elif cmd == "F":
                board = fill_pixel(board, *args)

            elif cmd == "S":
                save_array(board, *args)

            elif cmd == "C":
                board = clean_array(board)

            print(string(board))

        except:
            print("\nComando inválido!\n")


if __name__ == '__main__':
    main()
