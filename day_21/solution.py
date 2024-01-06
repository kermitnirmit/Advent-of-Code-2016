import itertools
from collections import defaultdict, deque
# from blist import *
import numpy as np
import parse

f = open("input.txt").read().splitlines()


# swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
# swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
# rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
# rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
# reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
# move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
s = "abcdefgh"
# s = "fbgdceah"
s = list(s)
# s = deque(s)


def scramble(s="abcdefgh"):
    s = list(s)
    for line in f:
        if line.startswith("move"):
            i, j = parse.parse("move position {:d} to position {:d}", line)
            add_back = s.pop(i)
            s.insert(j, add_back)
        elif line.startswith("swap"):
            if "position" in line:
                i, j = parse.parse("swap position {:d} with position {:d}", line)
                a = s[i]
                b = s[j]
                s[i] = b
                s[j] = a
            else:
                # print(line)
                a, b = parse.parse("swap letter {} with letter {}", line)
                # print(a,b)
                aindex = s.index(a)
                bindex = s.index(b)
                s[bindex] = a
                s[aindex] = b
        elif line.startswith("rotate"):
            if "based" in line:
                a = line[-1]
                q = s.index(a)
                s = deque(s)
                if q >= 4:
                    s.rotate(q+2)
                else:
                    s.rotate(q+1)
                s = list(s)
            else:
                a, c, _ = parse.parse("rotate {} {:d} {}", line)
                sign = 1 if a == "right" else -1
                s = deque(s)
                s.rotate(sign * c)
                s = list(s)
        else:
            a, b = parse.parse("reverse positions {:d} through {:d}", line)
            s[a:b + 1] = s[a:b + 1][::-1]
        # print(line, "after: ", "".join(s))
    return s

target = list("fbgdceah")
for a in itertools.permutations("abcdefgh"):
    if scramble() == target:
        print("".join(a))
        break
