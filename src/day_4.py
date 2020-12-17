import re

from utils import load_day


def parse_passport(passport):
    codes = re.findall(r'(.+?):(.+?)(?:\s|$)', passport)
    return dict(codes)


def valid_range(low, high):
    def _inner(x):
        try:
            return low <= int(x) <= high
        except ValueError:
            return False
    return _inner


def check_height(x):
    if x.endswith('cm'):
        return HEIGHT_CM_FN(x.replace('cm', ''))
    elif x.endswith('in'):
        return HEIGHT_IN_FN(x.replace('in', ''))
    else:
        return False


def regex_match(r):
    return lambda x, r=r: bool(re.fullmatch(r, x))


REQUIRED_CODES = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
EYE_CODES = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
HEIGHT_CM_FN = valid_range(150, 193)
HEIGHT_IN_FN = valid_range(59, 76)


day_four_input = load_day(4, sample=False, split=False)

# Part 1
n_valid = 0
for passport in day_four_input.split('\n\n'):
    codes = parse_passport(passport).keys()
    missing_codes = REQUIRED_CODES - set(codes)
    n_valid += len(missing_codes) == 0


print(f'Part 1: {n_valid}')


# Part 2
IS_VALID_FNS = {
    'byr': valid_range(1920, 2002),
    'iyr': valid_range(2010, 2020),
    'eyr': valid_range(2020, 2030),
    'hgt': check_height,
    'hcl': regex_match(r'#[\dabcdef]{6}'),
    'ecl': lambda x: x in EYE_CODES,
    'pid': regex_match(r'\d{9}'),
}

n_valid = 0
for passport in day_four_input.split('\n\n'):
    pairs = parse_passport(passport)
    missing_codes = REQUIRED_CODES - set(pairs.keys())
    if len(missing_codes) == 0:
        n_valid += all(IS_VALID_FNS[code](pairs[code]) for code in REQUIRED_CODES)

print(f'Part 2: {n_valid}')
