import numpy as np
from scipy import ndimage

from utils import load_day


start_board = load_day(17)


def parse_initial_board(start_board, pad=6):
    n = len(start_board)
    mn = n + 2 * pad
    board = np.zeros((mn, mn, mn, mn))
    for row in start_board:
        for x in range(n):
            for y in range(n):
                board[pad, pad, x+pad, y+pad] = start_board[x][y] == '#'
    return board


def run_cube_rules(board, k, n):
    for i in range(n):
        n_neighbors = ndimage.convolve(board, k, mode='constant')
        remains_active = (board != 0.0) & ((n_neighbors == 2) | (n_neighbors == 3))
        becomes_active = np.logical_not(board) & (n_neighbors == 3)
        board = (remains_active | becomes_active).astype(float)
    return board


# Part 1
k = np.ones((3, 3, 3))
k[1, 1, 1] = 0
board = run_cube_rules(parse_initial_board(start_board)[6], k, 6)
print(f'Part 1: {int(board.sum())}')


# Part 2
k = np.ones((3, 3, 3, 3))
k[1, 1, 1, 1] = 0
board = run_cube_rules(parse_initial_board(start_board), k, 6)
print(f'Part 2: {int(board.sum())}')