import re
from collections import Counter, deque
from copy import copy

from parse import parse
import hashlib

# f = open("input.txt").read().splitlines()

# Call the data you have at this point "a".
# Make a copy of "a"; call this copy "b".
# Reverse the order of the characters in "b".
# In "b", replace all instances of 0 with 1 and all 1s with 0.
# The resulting data is "a", then a single 0, then "b".

def flip_bits(s):
    news = ""
    for char in s:
        if char == "1":
            news += "0"
        else:
            news += "1"
    return news

def dragon(a):
    b = copy(a)
    b = b[::-1]
    b = flip_bits(b)
    return  a + "0" + b

def produce_sum(s):
    ret = ""
    for i in range(0, len(s), 2):
        left, right = s[i], s[i+1]
        if left == right:
            ret += "1"
        else:
            ret += "0"
    if len(ret) % 2 != 0:
        return ret
    else:
        return produce_sum(ret)

def solve(p2=False):
    checksumlen = 35651584 if p2 else 272
    a = "10111100110001111"
    while len(a) < checksumlen:
        a = dragon(a)
    return produce_sum(a[:checksumlen])
print(solve())
print(solve(True))