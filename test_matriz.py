from textwrap import dedent
from matriz import create_array, string, clean_array


def test_create():
    board = create_array(['4', '5'])
    assert string(board) == dedent(
    '''\
    OOOO
    OOOO
    OOOO
    OOOO
    OOOO'''
    )

def test_clean():
    board = create_array(['4','5'], 'X')
    board = clean_array(board)
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )


'''
def string(board):
    return '\n'.join((''.join(row) for row in board))
'''

'''
def test_create():
    board = create_array(['4','5'])

    assert len(board) == 5 and len(board[0]) == 4
'''