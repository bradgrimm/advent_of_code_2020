from utils import load_day


day_five_input = load_day(5)
half_fn = lambda x, i: x[i]

def half(pos, is_high):
    low, high = pos
    h = (high - low) // 2
    return (high - h, high) if is_high else (low, low + h)


def find_seat(part):
    row, col = (1, 128), (1, 8)
    for c in part:
        if c == 'F' or c == 'B':
            row = half(row, c == 'B')
        elif c == 'L' or c == 'R':
            col = half(col, c == 'R')
    return row[0] - 1, col[0] - 1


# Part 1
max_seat = 0
all_seat_ids = []
for row in day_five_input:
    row = find_seat(row)
    seat_id = row[0] * 8 + row[1]
    all_seat_ids.append(seat_id)
    max_seat = max(seat_id, max_seat)

print(f'Part 1: {max_seat}')


# Part 2
all_seat_ids = set(all_seat_ids)
for i in range(max_seat):
    if i not in all_seat_ids and i >= 15:
        break
print(f'Part 2: {i}')
