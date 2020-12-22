import numpy as np

from utils import load_day

data = load_day(22, split=False).split('\n\n')
p1_data = [int(c) for c in data[0].split('\n')[1:][::-1]]
p2_data = [int(c) for c in data[1].split('\n')[1:][::-1]]


def play_simple_game(p1_data, p2_data):
    p1_data, p2_data = list(p1_data), list(p2_data)
    while p1_data and p2_data:
        c1, c2 = p1_data.pop(), p2_data.pop()
        arr = p1_data if c1 > c2 else p2_data
        arr[0:0] = [min([c1, c2]), max(c1, c2)]
    return p1_data or p2_data


def score_hand(arr):
    values = np.array(arr) * np.array(range(1, len(arr) + 1))
    return values.sum()


# Part 1
winning_hand = play_simple_game(p1_data, p2_data)
print(f'Part 1: {score_hand(winning_hand)}')


def hand_id(d):
    return ' '.join([str(v) for v in d])


def play_game(p1_data, p2_data):
    has_seen = set()
    p1_data, p2_data = list(p1_data), list(p2_data)
    while p1_data and p2_data:
        # Infinite recursion check.
        game_id = hand_id(p1_data) + 'X' + hand_id(p2_data)
        if game_id in has_seen:
            return True, p1_data
        has_seen.add(game_id)
        
        # Game rules
        c1, c2 = p1_data.pop(), p2_data.pop()
        if len(p1_data) >= c1 and len(p2_data) >= c2:
            p1_winner, _ = play_game(p1_data[-c1:], p2_data[-c2:])
        else:
            p1_winner = c1 > c2
        if p1_winner:
            p1_data[0:0] = [c2, c1]
        else:
            p2_data[0:0] = [c1, c2]
    winning_deck = p1_data or p2_data
    return len(p1_data) > 0, winning_deck


# Part 2
_, winning_hand = play_game(p1_data, p2_data)
print(f'Part 2: {score_hand(winning_hand)}')
