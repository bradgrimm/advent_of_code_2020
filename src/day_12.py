from math import cos, sin

import numpy as np

from utils import load_day


def rotate(x, y, degrees):
    theta = np.deg2rad(degrees)
    xp = x * cos(theta) - y * sin(theta)
    yp = x * sin(theta) + y * cos(theta)
    return round(xp), round(yp)


dirs = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}
commands = load_day(12, sample=False)

# Part 1
x, y = 0, 0
hx, hy = 1, 0
for command in commands:
    cmd, amt = command[0], int(command[1:])
    if cmd in ('N', 'S', 'E', 'W'):
        dx, dy = dirs[cmd]
        x += dx * amt
        y += dy * amt
    elif cmd in ('L', 'R'):
        degrees = amt if cmd == 'L' else -amt
        hx, hy = rotate(hx, hy, degrees)
    elif cmd == 'F':
        x += hx * amt
        y += hy * amt
print(f'Part 1: {abs(x) + abs(y)}')


# Part 2
x, y = 0, 0
wx, wy = 10, 1
for command in commands:
    cmd, amt = command[0], int(command[1:])
    if cmd in ('N', 'S', 'E', 'W'):
        dx, dy = dirs[cmd]
        wx += dx * amt
        wy += dy * amt
    elif cmd in ('L', 'R'):
        degrees = amt if cmd == 'L' else -amt
        wx, wy = rotate(wx, wy, degrees)
    elif cmd == 'F':
        x += wx * amt
        y += wy * amt
print(f'Part 2: {abs(x) + abs(y)}')
