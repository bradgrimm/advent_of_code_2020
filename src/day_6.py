from utils import load_day


day_six_input = load_day(6, sample=False, split=False).split('\n\n')

# Part 1
n = 0
for group in day_six_input:
    c = set.union(*(set(row) for row in group.split()))
    n += len(c)
print(f'Part 1: {n}')

# Part 2
n = 0
for group in day_six_input:
    c = set.intersection(*(set(row) for row in group.split()))
    n += len(c)
print(f'Part 2: {n}')