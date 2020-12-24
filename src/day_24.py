from collections import defaultdict

import numpy as np
from scipy.signal import convolve2d

from utils import load_day

commands = load_day(24)
all_tiles = defaultdict(bool)
dirs = {
    'ne': (1, 1), 'nw': (-1, 1),
    'e': (2, 0), 'w': (-2, 0),
    'se': (1, -1), 'sw': (-1, -1),
}
neighbor_kern = np.array([
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]).transpose()


def turn_tile(cmd):
    idx, pos = 0, np.array([0, 0])
    while idx < len(cmd):
        if cmd[idx] in ('n', 's'):
            mv = dirs[cmd[idx:idx+2]]
            idx += 2
        else:
            mv = dirs[cmd[idx]]
            idx += 1
        pos += mv
    return tuple(pos)


def tiles_to_board(tiles):
    tiles = all_tiles.keys()

    x = np.array([t[0] for t in tiles])
    y = np.array([t[1] for t in tiles])
    w = (x.max() - x.min()) + 1
    h = (y.max() - y.min()) + 1

    board = np.zeros([w, h])
    for pos, is_black in all_tiles.items():
        tx = pos[0] - x.min()
        ty = pos[1] - y.min()
        board[tx, ty] = is_black
    return board.astype(int)


def flip_tiles(board):
    n_neighbors = convolve2d(board, neighbor_kern).astype(int)
    pad_board = np.pad(board, [(2, 2), (1, 1)]).astype(int)
    to_white = pad_board & ((n_neighbors == 0) | (n_neighbors > 2))
    to_black = np.logical_not(pad_board) & (n_neighbors == 2)
    pad_board[to_white.astype(bool)] = False
    pad_board[to_black.astype(bool)] = True
    return pad_board


# Part 1
for d in commands:
    pos = turn_tile(d)
    all_tiles[pos] = not all_tiles[pos]
print(f'Part 1: {sum(all_tiles.values())}')


# Part 2
board = tiles_to_board(all_tiles.keys())
for i in range(100):
    board = flip_tiles(board)
print(f'Part 2: {board.sum()}')
