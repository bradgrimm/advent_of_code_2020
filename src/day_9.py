from collections import deque
from itertools import combinations

from utils import load_day

is_sample = False
day_nine_input = load_day(9, sample=is_sample)
day_nine_input = [int(v) for v in day_nine_input]
preamble = 5 if is_sample else 25
values = day_nine_input


# Part 1
def is_valid(v, arr):
    return any([v == sum(p) for p in combinations(arr, 2)])

for idx in range(preamble, len(values)-1):
    v = values[idx]
    p_arr = values[idx-preamble:idx]
    if not is_valid(v, p_arr):
        break

invalid_value = v
print(f'Part 1: {invalid_value}')


# Part 2
current_sum = 0
low, high = (0, 0)
while current_sum != invalid_value:
    if current_sum < invalid_value:
        high += 1
        current_sum += values[high-1]
    elif current_sum > invalid_value:
        low += 1
        current_sum -= values[low-1]

low_plus_high = min(values[low:high]) + max(values[low:high])

print(f'Part 2: {low_plus_high}')
