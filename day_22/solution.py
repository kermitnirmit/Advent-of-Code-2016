import itertools
from collections import defaultdict, deque
import numpy as np
import parse
import utils

f = open("input.txt").read().splitlines()

w = {}

for line in f[2:]:
    x,y,s,u,a,_ = utils.ints(line)
    # print(x,y,s,u,a)
    w[(x,y)] = (s,u,a,_)
# print(w)

c = 0

def are_adjacent(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    # Check if the points are adjacent in a 2D space (4-directional movement)
    if abs(x1 - x2) == 1 and y1 == y2:
        return True
    elif abs(y1 - y2) == 1 and x1 == x2:
        return True
    else:
        return False

# (size, used, available)
# (Size  Used  Avail  Use%)
for a,b in itertools.permutations(w.keys(), 2):
    # Node A is not empty (its Used is not zero).
    # Nodes A and B are not the same node.
    # The data on node A (its Used) would fit on node B (its Avail).
    if w[a][1] != 0 and w[a][1] <= w[b][2]:
        c += 1
print(c)

miny = 0
minx = 0
maxx = max(x[0] for x in w.keys())
maxy = max(x[1] for x in w.keys())

# x goes across, y goes down
grid = []
for i in range(maxy+1):
    row = []
    for j in range(maxx + 1):
        if (j,i) in w:
            row.append(w[(j,i)][:-1])
        else:
            row.append("x")
    print(row)
    grid.append(row)

for k,v in w.items():
    if v[1] == 0:
        print(k, v)