from utils import load_day

equations = load_day(18)


def find_closing_parens(s, idx, n_parens=1):
    lookup = {'(': 1, ')': -1}
    while n_parens >= 1:
        n_parens += lookup.get(s[idx], 0)
        idx += 1
    return idx - 1


def find_closing_space(s, idx):
    try:
        return s.index(' ', idx)
    except ValueError:
        return len(s)


def to_int_or_symbol(eq):
    try:
        return int(eq)
    except ValueError:
        return eq.strip()

    
def evaluate_equation(eq, eval_fn):
    idx = 0
    eq_parts = []
    while idx < len(eq):
        c = eq[idx]
        if c == '(':
            end_idx = find_closing_parens(eq, idx+1) + 1
            ret_value = evaluate_equation(eq[idx+1:end_idx-1], eval_fn)
        else:
            end_idx = find_closing_space(eq, idx)
            ret_value = eq[idx:end_idx]
        eq_parts.append(ret_value)
        idx = end_idx + 1
    return eval_fn(eq_parts)


# Part 1
def eval_left_to_right(arr):
    value, opp = 0, '+'
    for nv in arr:
        if nv in ['+', '*']:
            opp = nv
        elif opp == '+':
            value += int(nv)
        elif opp == '*':
            value *= int(nv)
    return value


total = sum([
    evaluate_equation(eq, eval_left_to_right)
    for eq in equations
])
print(f'Part 1: {total}')


# Part 2
def eval_add_then_mult(arr, idx=1):
    while idx < len(arr) - 1:
        prev, opp, nxt = arr[idx-1:idx+2]
        if opp == '+':
            value = int(prev) + int(nxt)
            arr = arr[:idx-1] + [value] + arr[idx+2:]
            idx = 0
        idx += 1
    return eval_left_to_right(arr)


total = sum([
    evaluate_equation(eq, eval_add_then_mult)
    for eq in equations
])
print(f'Part 2: {total}')