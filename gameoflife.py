from matriz import create_array, set_many, string

DEAD = chr(0x00B7)
LIVE = chr(0x2588)

GLIDER = ((2,1), (3,2), (1,3), (2,3), (3,3))

def main():
    board = []
    create_array(board, 50, 25, DEAD)
    set_many(board, GLIDER, LIVE)

    print(string(board))




if __name__ == '__main__':
    main()