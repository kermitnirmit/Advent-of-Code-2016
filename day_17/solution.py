import re
from collections import Counter, deque
from copy import copy

from parse import parse
import hashlib

# f = open("input.txt").read().splitlines()

from utils import dmap, add_tuples

dirs = ["U", "D", "L", "R"]

def get_dirs(s):
    output = hashlib.md5(s.encode()).hexdigest()[:4]

     # up, down, left, and right from your current position.
    # Any b, c, d, e, or f means that the corresponding door is open;
    ret = []
    for i in range(len(output)):
        if output[i] in "bcdef":
            ret.append(dirs[i])
    return ret


q = [((0,0), "")]

q = deque(q)

v = set()
goal = (3,3)
secret = "hhhxzeay"
paths = []
while q:
    curr, path = q.popleft()
    if curr == goal:
        paths.append(path)
        continue
    if (curr, path) in v:
        continue
    else:
        v.add((curr, path))
        for dir in get_dirs(secret + path):
            di, dj = dmap[dir]
            ni, nj = add_tuples(curr, (di, dj))
            if 0 <= ni <= 3 and 0 <= nj <= 3:
                q.append(((ni, nj), path + dir))
# print(get_dirs("hijklDR"))

# p1: DDRUDLRRRD
maxlenIndex = 0
maxLen = 0
for i, path in enumerate(paths):
    if len(path) > maxLen:
        maxlenIndex = i
        maxLen = len(path)
print(maxLen)