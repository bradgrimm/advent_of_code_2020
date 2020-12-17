from itertools import combinations

from utils import load_day

# Part 1
day_one_input = {int(v) for v in load_day(1)}
for n in day_one_input:
    paired_value = 2020 - n
    if paired_value in day_one_input:
        break

print('Part 1: {}'.format(n * paired_value))


# Part 2
day_one_input = [int(v) for v in load_day(1)]
for combo in combinations(day_one_input, 3):
    if sum(combo) == 2020:
        break


print('Part 2: {}'.format(combo[0] * combo[1] * combo[2]))
