import numpy as np

from utils import load_day


day_3_map = load_day(3)
def traverse_mountain(dx, dy, x=0, y=0):
    w = len(day_3_map[0])
    n_trees = 0
    while y < len(day_3_map):
        if day_3_map[y][x] == '#':
            n_trees += 1
        x, y = (x + dx) % w, (y + dy)
    return n_trees


# Part 1
trees = traverse_mountain(3, 1)
print('Part 1: {}'.format(trees))


# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
all_trees = np.prod([traverse_mountain(*s) for s in slopes])
print('Part 2: {}'.format(all_trees))