import itertools
from copy import copy

import math
from collections import defaultdict, deque
from parse import parse
from utils import add_tuples

f = open("input.txt").read().strip().splitlines()

targets = set()

start = None
dirs_2d_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == "0":
            start = (i, j)
        if f[i][j] in "0123456789":
            targets.add((i, j))

q = [(start, set(), set(), 0)]
q = deque(q)
seen = set()
c = 0

dist_graph = defaultdict(dict)


def bfs(start, target):
    q = [(start, 0)]
    q = deque(q)
    seen = set()
    while q:
        curr, dist = q.popleft()
        if curr == target:
            return dist
        if curr in seen:
            continue
        else:
            seen.add(curr)
            for d in dirs_2d_4:
                ni, nj = add_tuples(curr, d)
                if 0 <= ni < len(f) and 0 <= nj < len(f[0]) and f[ni][nj] != "#":
                    q.append(((ni, nj), dist + 1))


for a, b in itertools.combinations(targets, 2):
    dist = bfs(a, b)
    dist_graph[a][b] = dist
    dist_graph[b][a] = dist


targets_without_start = set(filter(lambda x: x != (start), targets))

c = math.inf
for ordering in itertools.permutations(targets_without_start, len(targets_without_start)):
    t = 0
    ordering = [(start)] + list(ordering)
    for a,b in zip(ordering, ordering[1:]):
        t += dist_graph[a][b]
    c = min(c, t)
    # break
print(c)

c = math.inf
for ordering in itertools.permutations(targets_without_start, len(targets_without_start)):
    t = 0
    ordering = [(start)] + list(ordering) + [(start)]
    for a,b in zip(ordering, ordering[1:]):
        t += dist_graph[a][b]
    c = min(c, t)
    # break
print(c)