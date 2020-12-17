import re
from collections import defaultdict

from utils import load_day

day_seven_input = load_day(7, sample=False, split=True)


parents = defaultdict(set)
children = defaultdict(set)
for row in day_seven_input:
    bag = re.match(r'(.+) bags contain', row).groups()[0]
    for count, child in re.findall(r'(\d) (.+?) bag', row):
        parents[child].add(bag)
        children[bag].add((int(count), child))


# Part 1
to_check = ['shiny gold']
valid_bags = set()
while to_check:
    bag = to_check.pop()
    valid_bags.add(bag)
    to_check.extend(parents[bag])
print(f'Part 2: {len(valid_bags) - 1}')


# Part 2
to_add = [(1, 'shiny gold')]
total = 0
while to_add:
    p_num, bag = to_add.pop()
    total += p_num
    for c_num, child in children[bag]:
        to_add.append((p_num * c_num, child))
print(f'Part 2: {total - 1}')
