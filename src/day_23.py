from utils import load_day


cups = load_day(23, split=False)
cups = [int(c) for c in cups]


def parse_part_1_graph(cups):
    n = len(cups)
    graph = {cups[i]: cups[i+1] for i in range(n-1)}
    graph[cups[-1]] = cups[0]
    return graph


def parse_part_2_graph(cups, sz=1000000):
    graph = parse_part_1_graph(cups)
    ms = max(cups) + 1
    for i in range(ms, sz+1):
        graph[i] = i + 1
    graph[cups[-1]] = ms
    graph[sz] = cups[0]
    return graph


def cups_to_list(n, v=1):
    arr = []
    for _ in range(n):
        v = graph[v]
        arr.append(v)
    return arr


def play_cup_game(n_rounds=100):
    max_val = max(graph.keys())
    orig_val = cups[0]
    for _ in range(n_rounds):
        v = orig_val
        pickup = [(v := graph[v]) for _ in range(3)]
        dst_val = orig_val - 1
        while dst_val in pickup or dst_val == 0:
            dst_val = (dst_val - 1) % (max_val + 1)
        
        graph[orig_val] = graph[pickup[-1]]
        graph[pickup[-1]] = graph[dst_val]
        graph[dst_val] = pickup[0]
        orig_val = graph[orig_val]


# Part 1
graph = parse_part_1_graph(cups)
play_cup_game(100)
cup_order = cups_to_list(8)
score = ''.join([str(c) for c in cup_order])
print(f'Part 1: {score}')


# Part 2
graph = parse_part_2_graph(cups)
play_cup_game(10000000)
values = cups_to_list(2)
score = int(values[0]) * int(values[1])
print(f'Part 2: {score}')