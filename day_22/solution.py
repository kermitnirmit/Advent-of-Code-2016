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

# 24 + 2 directly there
# the wall makes you go 23 steps to the left
# so it takes you 23 + 23 + 24 + 2 steps to get to the target data.
# shifting that data over by one takes 5 steps. 36 more steps so 36*5
print(23 + 23 + 24 + 2 + 5 * 36)
