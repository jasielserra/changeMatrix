# -*- coding: utf8 -*-
import sys
from collections import deque
from os import system

BLANK = "O"

def width(board):
    return len(board[0])

def height(board):
    return len(board)

def x(c):
    return c[0]

def y(c):
    return c[1]

def offset(coord, rel):
    return x(coord) + x(rel), y(coord) + y(rel)

def set_item(board, coord, value):
    board[y(coord) - 1][x(coord) - 1] = value

def get_item(board, coord):
    return board[y(coord) - 1][x(coord) - 1]

def string(board):
    return '\n'.join(("".join(row) for row in board))