from utils import load_day


def find_num_loops(key, value=1):
    n, subject_num = 0, 7
    while value != key:
        value = (value * subject_num) % 20201227
        n += 1
    return n


def transform_key(subject_num, loop_size, value=1):
    for _ in range(loop_size):
        value = (value * subject_num) % 20201227
    return value


door_key, card_key = load_day(25)
door_key, card_key = int(door_key), int(card_key)
door_loops = find_num_loops(door_key)
card_loops = find_num_loops(card_key)

door_enc_key = transform_key(door_key, card_loops)
card_enc_key = transform_key(card_key, door_loops)

assert door_enc_key == card_enc_key
print(f'Part 1: {door_enc_key}')