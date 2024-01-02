from collections import defaultdict
from parse import parse
f = open("input.txt").read().strip().splitlines()

reg = defaultdict(int)

q = 0
i = 0
reg["c"] = 1
while i < len(f):
    q += 1
    line = f[i]
    # print(reg, i, line)
    if line.startswith("cpy"):
        _, v, l = line.split()
        try:
            v = int(v)
        except:
            v = reg[v]
        reg[l] = v
    elif line.startswith("inc"):
        _, l = line.split()
        reg[l] += 1
    elif line.startswith("dec"):
        _, l = line.split()
        reg[l] -= 1
    elif line.startswith("jnz"):
        _, l, d = line.split()
        check = None
        try:
            check = int(l)
        except:
            if l not in reg:
                check = 0
            check = reg[l]
        if check != 0:
            i += int(d)
            continue
    i += 1
print(reg["a"])

# part 1: 318117

