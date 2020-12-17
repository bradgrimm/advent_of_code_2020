from collections import Counter, defaultdict

import numpy as np

from utils import load_day

day_ten_input = load_day(10, sample=False)
jolts = [int(d) for d in day_ten_input]


# Part 1
sort_jolts = [0] + sorted(jolts)
dj = np.array(sort_jolts[1:]) - np.array(sort_jolts)[:-1]
counts = Counter(dj)
print(f'Part 1: {(counts[3] + 1) * counts[1]}')


# Part 2
jolt_set = {0} | set(jolts)
options = defaultdict(lambda: 0, {max(jolt_set): 1})

for j in sorted(sort_jolts, reverse=True):
    for nj in range(j-1, j-4, -1):
        if nj in jolt_set:
            options[nj] += options[j]
print(f'Part 2: {options[0]}')
