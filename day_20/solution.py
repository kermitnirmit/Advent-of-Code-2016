from collections import defaultdict, deque
# from blist import *
import numpy as np

f = open("input.txt").read().splitlines()

ranges = []


# each range is a start, and a length. this list should be sorted.
for line in f:
    l, r = line.split("-")
    l = int(l)
    r = int(r)
    # print(l, r)
    length = r-l
    print(l, length)
    ranges.append((l, length))

def merge_ranges(ranges):
    # Sort the list of tuples based on the start values
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged_ranges = []
    current_start, current_end = sorted_ranges[0]

    for start, length in sorted_ranges[1:]:
        # Check for overlapping or half-overlapping ranges
        if start <= current_end + 1:
            # Merge ranges
            current_end = max(current_end, start + length)
        else:
            # Add the merged range to the result and update current range
            merged_ranges.append((current_start, current_end))
            current_start, current_end = start, start + length

    # Add the last merged range
    merged_ranges.append((current_start, current_end))

    return merged_ranges

newranges = merge_ranges(ranges)
c = 0
for a,b in zip(newranges, newranges[1:]):
    end = a[1]
    start = b[0]
    c += (start - end) - 1
print(c)