from math import gcd

from utils import load_day, arrow_alignment


data = load_day(13, split=False)


# Part 1
earliest, busses_str = data.split('\n')
earliest = int(earliest)
busses = [int(b) for b in busses_str.split(',') if b != 'x']

bus_id = None
to_check = earliest
while bus_id is None:
    for b in busses:
        if to_check % b == 0:
            bus_id = b
    to_check += 1

wait_time = (to_check - 1) - earliest
print(f'Part 1: {wait_time * bus_id}')


# Part 2
busses = [(n, int(b)) for n, b in enumerate(busses_str.split(',')) if b != 'x']

def lcm(x, y):
    return x * y // gcd(x, y)

def find_shifted_lcm(a, b, xs, ys):
    x_shift = arrow_alignment(a, b, xs + ys) - xs
    x_mult = lcm(a, b)
    return (x_shift, x_mult)


xs, xm = busses[0]
for ys, ym in busses[1:]:
    xs, xm = find_shifted_lcm(xm, ym, -xs, -ys)
print(f'Part 2: {xs}')
