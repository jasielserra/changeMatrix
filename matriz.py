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


def print_board(board):
    """Print the Board."""
    print("\n")
    print(string(board))
    print("\n")


def create_array(cmd, value=BLANK):
    """Create a array - 'I' Command."""
    col, row = int(cmd[0]), int(cmd[1]) # TODO
    return [[value] * col for _ in range(row)]


def clean_array(board, value=BLANK):
    """ Clean a array - 'C' Command."""
    # TODO: range conhece muito sobre a estrutura do board.
    for row in range(1, height(board) + 1):
        for col in range(1, width(board) + 1):
            set_item(board, (col, row), value)
    return board


def color_pixel(cmd, board):
    """ Change the color of one pixel - 'L' Command. """
    coord, color = (int(cmd[0]), int(cmd[1])), cmd[2] #TODO
    set_item(board, coord, color)

    return board


def ver_pixel(cmd, board):
    """Change the color of a column - 'V' Command."""
    col, row_start, row_end, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), cmd[3]

    for row in range(row_start, row_end + 1):
        set_item(board, (col, row), color)
    return board


def hor_pixel(cmd, board):  # Change the color of a line - 'H' Command.
    colIni, colEnd, line, color = cmd

    for hor in range(int(colIni) - 1, int(colEnd)):
        board[int(line) - 1][int(hor)] = color
    return board


def block_pixel(cmd, board):  # Change color of an entire block - 'K' Command.
    colIni, lineIni, colEnd, lineEnd, color = cmd

    for hor in range(int(colIni) - 1, int(colEnd)):
        for ver in range(int(lineIni) - 1, int(lineEnd)):
            board[int(ver)][int(hor)] = color
    return board


def out_range(board, Y, X):  # Check if a cmd is out of list range.
    line = len(board)
    col = len(board[0])

    if (X >= 0 and X < col) and (Y >= 0 and Y < line):
        return True
    else:
        return False


def fill_pixel(cmd, board):  # Fill a continuous region 'F' command.
    col, line, chgColor = cmd

    color = board[line][col]

    if out_range(board, line, col):
        board[line][col] = chgColor

        if out_range(board, line, col - 1):
            if board[line][col - 1] == color:
                fill_pixel([col - 1, line, chgColor], board)

        if out_range(board, line, col + 1):
            if board[line][col + 1] == color:
                fill_pixel([col + 1, line, chgColor], board)

        if out_range(board, line - 1, col):
            if board[line - 1][col] == color:
                fill_pixel([col, line - 1, chgColor], board)

        if out_range(board, line + 1, col):
            if board[line + 1][col] == color:
                fill_pixel([col, line + 1, chgColor], board)

    return board


def save_array(name, board):  # Save the array with the 'S' command.
    with open(name.lower(), "w") as my_file:
        for item in board:
            my_file.write("".join(item) + "\n")

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
                cmd[1] = int(cmd[1]) - 1
                cmd[2] = int(cmd[2]) - 1
                board = fill_pixel(cmd[1:4], board)

            elif cmd[0] == "S":
                save_array(cmd[1], board)

            elif cmd[0] == "C":
                board = clean_array(board)

            else:
                continue

            print_board(board)

        except:
            print("\nComando inválido!\n")


if __name__ == '__main__':
    main()
