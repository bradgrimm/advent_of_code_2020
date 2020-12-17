from collections import defaultdict

import numpy as np

from utils import load_day

data = load_day(16, split=False)


# Part 1
values, your_ticket, nearby_tickets = data.split('\n\n')
your_ticket = np.array([int(v) for v in your_ticket.split('\n')[1].split(',')])
def str_to_range(r):
    return tuple(int(v) for v in r.split('-'))


def find_all_ranges(values):
    all_ranges = {}
    for row in values.split('\n'):
        name, criteria = row.split(':')
        small, _, large = criteria.split()
        all_ranges[name] = [str_to_range(small), str_to_range(large)]
    return all_ranges


def valid_range(v, ranges):
    return any(r[0] <= v <= r[1] for r in ranges)


range_dict = find_all_ranges(values)
bad_values = []
valid_tickets = []
for ticket in nearby_tickets.split('\n')[1:]:
    is_valid = True
    for v in ticket.split(','):
        v = int(v)
        if not any(valid_range(v, r) for r in range_dict.values()):
            bad_values.append(v)
            is_valid = False
    if is_valid:
        valid_tickets.append(ticket)
print(f'Part 1: {sum(bad_values)}')


# Part 2
def find_possible_columns(tickets, range_dict):
    is_possible = defaultdict(lambda: defaultdict(lambda: True))
    # Invalidate columns based on value.
    for ticket in tickets:
        for idx, ticket_value in enumerate(ticket.split(',')):
            for k, r in range_dict.items():
                if not valid_range(int(ticket_value), r):
                    is_possible[k][idx] = False
    # Find remaining valid values.
    for k, v in is_possible.items():
        v = set(v.keys())
        is_possible[k] = [i for i in range(len(your_ticket)) if i not in v]
    return is_possible


def find_columns_by_elimination(is_possible):
    tags = {}
    while len(tags) < len(is_possible):
        for key, items in is_possible.items():
            unassigned = [p for p in items if p not in tags]
            if len(unassigned) == 1:
                tags[unassigned[0]] = key
    return tags


is_possible = find_possible_columns(valid_tickets, range_dict)
tags = find_columns_by_elimination(is_possible)
departure_idx = np.array([k for k, v in tags.items() if v.startswith('departure')])
ticket_values = np.prod(your_ticket[departure_idx])
print(f'Part 2: {ticket_values}')
