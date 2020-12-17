import numpy as np
from scipy.signal import convolve2d

from utils import load_day


rows = load_day(11)
mapping = {'.': 0, 'L': 1, '#': 2}
seats = np.array([[mapping[c] for c in r] for r in rows])


def find_equilibrium(neighbor_fn, n_allowed=4):
    occupied = np.zeros_like(seats)
    next_round = np.array(seats)
    while np.abs(next_round - occupied).sum() > 0:
        occupied = next_round
        n_neighbors = neighbor_fn(occupied)
        filled = (n_neighbors == 0)
        remained = (occupied & (n_neighbors < n_allowed))
        next_round = seats & (filled | remained)
    return next_round.sum()


# Part 1
sum_kernel = np.ones((3, 3))
sum_kernel[1, 1] = 0
def find_neighbors(occupied):
    return convolve2d(occupied, sum_kernel, 'same')

n_seats = find_equilibrium(find_neighbors, n_allowed=4)
print(f'Part 1: {n_seats}')


# Part 2
w, h = len(rows[0]), len(rows)
dirs = [
    (dx, dy)
    for dx in range(-1, 2)
    for dy in range(-1, 2)
    if (dx, dy) != (0, 0)
]
is_invalid = lambda x, y: x < 0 or x >= w or y < 0 or y >= h
def count_neighbors(occupied, neighbors, sx, sy):
    for dx, dy in dirs:
        x, y = int(sx), int(sy)
        while not is_invalid(x + dx, y + dy):
            x, y = (x + dx), (y + dy)
            if seats[x, y] == 1:
                neighbors[sx, sy] += occupied[x, y]
                break

def find_visible_neighbors(occupied):
    neighbors = np.zeros_like(occupied)
    for sx in range(w):
        for sy in range(h):
            count_neighbors(occupied, neighbors, sx, sy)
    return neighbors

n_seats = find_equilibrium(find_visible_neighbors, 5)
print(f'Part 2: {n_seats}')
