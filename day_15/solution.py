import re
from collections import Counter, deque
from parse import parse
import hashlib

f = open("input.txt").read().splitlines()
def solve(p2=False):
    q = []
    for line in f:
        _, num_positions, start = parse("Disc #{:d} has {:d} positions; at time=0, it is at position {:d}.", line)
        q.append((int(num_positions), int(start)))
    if p2:
        q.append((11, 0))
    w = []

    p = 1
    for index, val in enumerate(q):
        num_positions, start = val

        time = index + 1

        where_it_should_be_at_time = num_positions - time
        w.append((where_it_should_be_at_time - start) % num_positions)
        # num_positions - time # is where it needs to be at t= 0... so i need to know how far away from current that is...

        p *= num_positions

    for i in range(1, p):
        if all(i % x[0][0] == x[1] for x in zip(q,w)):
            return i
            break
# 192996 is too high
# 121834 is right
print(solve(False))
print(solve(True))