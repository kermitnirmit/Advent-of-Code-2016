from collections import defaultdict, deque
# from blist import *
import numpy as np
def solve(n=3018458):
    c = [True] * n
    q = 0
    falses = 0
    while falses < len(c) - 1:
        w = q + 1
        w %= len(c)
        found = False
        while not found:
            if c[w]:
                found = True
            else:
                w += 1
                w %= len(c)
        c[w] = False
        falses += 1
        found = False
        q = w + 1
        q %= len(c)
        while not found:
            if c[q]:
                found = True
            else:
                q += 1
                q %= len(c)
        # print(q, w)
    for i, v in enumerate(c):
        if v:
            print(i + 1)

# solve()
# https://www.reddit.com/user/aceshades
def solve_2(n=3018458):
        l = deque()
        r = deque()

        for i in range(1, n+1):
            if i < n // 2 + 1:
                l.append(i)
            else:
                r.appendleft(i)
        while l and r:
            if len(l) > len(r):
                l.pop()
            else:
                r.pop()
            r.appendleft(l.popleft())
            l.append(r.pop())
        return l[0] or r[0]


print(solve_2())
 #    1
 # 6     2
 # 5     3
 #    4

 #   1
 # 6    2
 # 5   3

#   1
# 6    2
#   3

# trying 26735