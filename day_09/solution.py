import math
import re
import numpy as np
f = open("input.txt").read().strip().split("\n")[0]


def solve(f):
    builder = ""
    i = 0
    groups = re.finditer("\(\d*x\d*\)", f)
    d = {}
    for a in groups:
        d[a.start()] = a.end()
    while i < len(f):
        if i in d.keys():
            qwer = (f[i + 1:d[i] - 1])
            x, y = qwer.split("x")
            x, y = int(x), int(y)
            chars_to_copy = f[d[i]:d[i] + x]
            chars_to_add = chars_to_copy * y
            builder += chars_to_add
            i = d[i] + len(chars_to_copy)
        else:
            builder += f[i]
            i += 1
    return len(builder), builder, len(builder)

def solve_p2(s):
    m = np.array([1 for _ in s])
    index = 0
    length = 0
    while index < len(s):
        char = s[index]
        if char == "(":
            close = s.find(")", index)
            numChars, times = s[index:close+1].split("x")
            numChars, times = int(numChars[1:]), int(times[:-1])

            start = close + 1
            m[start:start+numChars] *= times
            index = close + 1
        else:
            length += m[index]
            index += 1
    return length
print(solve(f)[0])
print(solve_p2(f))