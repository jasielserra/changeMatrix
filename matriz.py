# -*- coding: utf8 -*-
BLANK = "O"

def width(board):
    return len(board[0])

def height(board):
    return len(board)

def x(coord):
    return coord[0]

def y(coord):
    return coord[1]

def set_item(board, coord, value):
    board[y(coord) - 1][x(coord) - 1] = value

def get_item(board, coord):
    return board[y(coord) - 1][x(coord) - 1]

def region(col_start, row_start, col_end, row_end):
    for row in range(row_start, row_end + 1):
        for col in range(col_start, col_end + 1):
            yield col, row

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


def create_array(cmd, value=BLANK):
    """Create a array - 'I' Command."""
    col, row = int(cmd[0]), int(cmd[1]) # TODO
    return [[value] * col for _ in range(row)]


def clean_array(board, value=BLANK):
    """ Clean a array - 'C' Command."""
    # TODO: range conhece muito sobre a estrutura do board.
    set_many(board, coords_of(board), value)
    return board


def color_pixel(cmd, board):
    """ Change the color of one pixel - 'L' Command. """
    coord, color = (int(cmd[0]), int(cmd[1])), cmd[2] #TODO
    set_item(board, coord, color)

    return board


def ver_pixel(cmd, board):
    """Change the color of a column - 'V' Command."""
    col, row_start, row_end, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), cmd[3]
    set_many(board, region(col, row_start, col, row_end), color)
    return board


def hor_pixel(cmd, board):
    """Change the color of a line - 'H' Command."""
    col_start, col_end, row, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), cmd[3]
    set_many(board, region(col_start, row, col_end, row), color)
    return board


def block_pixel(cmd, board):
    """Change color of an entire block - 'K' Command."""
    col_start, row_start, col_end, row_end, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), int(cmd[3]), cmd[4]
    set_many(board, region(col_start, row_start, col_end, row_end), color)
    return board


def out_range(board, coord):
    """Check if a cmd is out of list range."""
    X = x(coord)
    Y = y(coord)

    line = len(board)
    col = len(board[0])

    if (X >= 0 and X < col) and (Y >= 0 and Y < line):
        return True
    else:
        return False


def fill_pixel(cmd, board):
    """ Fill a continuous region 'F' command."""
    col, row, new_color = int(cmd[0]), int(cmd[1]), cmd[2]

    old_color = get_item(board,(col,row))

    if out_range(board, row, col):
        set_item(board,(col,row), new_color)

        neighbor = (col - 1, row)
        if out_range(board, neighbor):
            if get_item(board, neighbor) == old_color:
                fill_pixel(list(neighbor) + [new_color], board)

        neighbor = (col + 1, row)
        if out_range(board, neighbor):
            if get_item(board, neighbor) == old_color:
                fill_pixel(list(neighbor) + [new_color], board)

        neighbor = (col, row - 1)
        if out_range(board, neighbor):
            if get_item(board, neighbor) == old_color:
                fill_pixel(list(neighbor) + [new_color], board)

        neighbor = (col, row + 1)
        if out_range(board, neighbor):
            if get_item(board, neighbor) == old_color:
                fill_pixel(list(neighbor) + [new_color], board)

    return board


def save_array(filename, board):
    """ Save the array with the 'S' command. """
    with open(filename, "w") as f:
        f.write(string(board))


def string(board):
    return '\n'.join(("".join(row) for row in board))


def main():
    while True:
        try:
            cmd = read_sequence()

            if cmd[0] == "X":
                break

            elif cmd[0] == "I":
                board = create_array(cmd[1:3])

            elif cmd[0] == "L":
                board = color_pixel(cmd[1:4], board)

            elif cmd[0] == "V":
                board = ver_pixel(cmd[1:5], board)

            elif cmd[0] == "H":
                board = hor_pixel(cmd[1:5], board)

            elif cmd[0] == "K":
                board = block_pixel(cmd[1:6], board)

            elif cmd[0] == "F":
                board = fill_pixel(cmd[1:4], board)

            elif cmd[0] == "S":
                save_array(cmd[1], board)

            elif cmd[0] == "C":
                board = clean_array(board)

            else:
                continue

            print(string(board))

        except:
            print("\nComando inválido!\n")


if __name__ == '__main__':
    main()
