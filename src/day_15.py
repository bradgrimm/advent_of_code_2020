from utils import load_day


intro_nums = load_day(15, split=False).split(',')


def play_memory_game(intro_nums, count_to):
    nums = {int(n): i+1 for i, n in enumerate(intro_nums[:-1])}
    n = int(intro_nums[-1])
    for i in range(len(nums) + 1, count_to):
        prev_n = n
        n = (
            i - nums[n]
            if n in nums else
            0
        )
        nums[prev_n] = i
    return n


# Part 1
n = play_memory_game(intro_nums, 2020)
print(f'Part 1: {n}')


# Part 2
n = play_memory_game(intro_nums, 30000000)
print(f'Part 2: {n}')