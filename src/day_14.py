import numpy as np

from utils import load_day


data = load_day(14)


def mask_to_int(mask):
    return int(''.join(mask), 2)

def bitmask(arr, c):
    return mask_to_int(['1' if v == c else '0' for v in arr])


# Part 1
regs = {}
for row in data:
    reg, value = row.split(' = ')
    if reg == 'mask':
        and_mask = bitmask(value, 'X')
        change_mask = np.bitwise_not(and_mask)
        change_value = mask_to_int([v if v != 'X' else '0' for v in value])
        or_mask = change_value & change_mask
    else:
        regs[reg] = (int(value) & and_mask) | or_mask
print(f'Part 1: {sum(regs.values())}')


# Part 2
def convert_iter_to_mask(masks, value):
    or_value = 0
    for j in range(0, len(masks)):
        if (value & (1 << j)) != 0:
            or_value |= 1 << masks[j]
    return or_value

def find_all_floating_values(mask_str, to_assign):
    masks = [i for i, v in enumerate(mask_str[::-1]) if v == 'X']
    return {
        convert_iter_to_mask(masks, i) | to_assign
        for i in range(1 << len(masks))
    }

regs = {}
for row in data:
    reg, value = row.split(' = ')
    if reg == 'mask':
        or_mask = bitmask(value, '1')
        and_mask = np.bitwise_not(bitmask(value, 'X'))
        floating_mask = value
    else:
        dst = reg[:-1].split('[')[1]
        masked_dst = (int(dst) & and_mask) | or_mask
        for r in find_all_floating_values(floating_mask, masked_dst):
            regs[r] = int(value)
print(f'Part 2: {sum(regs.values())}')