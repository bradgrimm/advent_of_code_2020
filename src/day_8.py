from utils import load_day


day_eight_input = load_day(8, sample=False)

commands = []
state_change = {
    'jmp': lambda x: (int(x), 0),
    'nop': lambda x: (1, 0),
    'acc': lambda x: (1, int(x)),
    'none': lambda x: (None, None),
}
instr_swap = {'jmp': 'nop', 'nop': 'jmp', 'acc': 'none'}

for d in day_eight_input:
    instr, num = d.split()
    primary = state_change[instr](num)
    secondary = state_change[instr_swap[instr]](num)
    commands.append([primary, secondary])


# Part 1
line, accum = 0, 0
visited = set()
while line not in visited:
    visited.add(line)
    d_line, d_acc = commands[line][0]
    line += d_line
    accum += d_acc
print(f'Part 1: {accum}')


# Part 2
paths = [(0, 0, False, set())]
while paths:
    line, accum, has_swapped, visited = paths.pop()
    if line == len(commands):
        break
    if line in visited or line < 0 or line > len(commands):
        continue
    visited.add(line)
    (dy, dv), (dy_alt, dv_alt) = commands[line]
    paths.append((line + dy, accum + dv, has_swapped, set(visited)))
    if not has_swapped and dy_alt is not None:
        paths.append((line + dy_alt, accum + dv_alt, True, set(visited)))
print(f'Part 2: {accum}')
