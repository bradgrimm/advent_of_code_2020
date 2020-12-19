from utils import load_day


def parse_rules_and_messages(rows, is_part_2=False):
    rules, messages = rows.split('\n\n')
    if is_part_2:
        rules += """\n8: 42 | 42 8\n11: 42 31 | 42 11 31"""
    rules = rules.strip().split('\n')
    messages = messages.split('\n')

    rules_dict = {}
    for row in rules:
        idx, rule = row.split(': ')
        rules_dict[idx] = [
            [r.replace('"', '') for r in p.split()]
            for p in rule.split(' | ')
        ]
    return rules_dict, messages


def is_valid(orig_msg, rules_dict):
    valid_options = [(r, orig_msg) for r in rules_dict['0']]
    while valid_options:
        rule, msg = valid_options.pop()
        option = rule[0]
        if option in ['a', 'b']:
            # if msg[0] == option:
            #     if len(rule) == 1 and len(msg) == 1:
            #         return True
            #     elif len(rule) >= 2 and len(msg) >= 2:
            #         valid_options.append((rule[1:], msg[1:]))
            if msg[0] == option:
                if len(rule) == 1:
                    if len(msg) == 1:
                        return True
                    continue
                elif len(msg) >= 2:
                    valid_options.append((rule[1:], msg[1:]))
            continue
        for nx in rules_dict[option]:
            next_option = nx + rule[1:]
            valid_options.append((next_option, msg))
    return False


rows = load_day(19, split=False)

# Part 1
rules_dict, messages = parse_rules_and_messages(rows)
num_valid = sum([is_valid(s, rules_dict) for s in messages])
print(f'Part 1: {num_valid}')


# Part 2
rules_dict, messages = parse_rules_and_messages(rows, is_part_2=True)
num_valid = sum([is_valid(s, rules_dict) for s in messages])
print(f'Part 2: {num_valid}')
