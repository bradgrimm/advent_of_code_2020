from collections import Counter

from utils import load_day

# Part 1
n_correct = 0
for d in load_day(2):
    criteria, password = d.split(': ')
    valid_range, letter = criteria.split()
    valid_range = tuple(int(t) for t in valid_range.split('-'))
    
    pass_count = Counter(password)
    actual_count = pass_count[letter]
    if actual_count >= valid_range[0] and actual_count <= valid_range[1]:
        n_correct += 1

print(f'Part 1: {n_correct}')


# Part 2
n_correct = 0
for d in load_day(2):
    criteria, password = d.split(': ')
    valid_range, letter = criteria.split()
    
    l, r = tuple(int(t) for t in valid_range.split('-'))
    if (password[l-1] == letter) ^ (password[r-1] == letter):
        n_correct += 1
print(f'Part 2: {n_correct}')
