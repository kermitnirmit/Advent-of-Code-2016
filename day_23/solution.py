import math
from collections import defaultdict
from parse import parse
f = open("input.txt").read().strip().splitlines()

reg = defaultdict(int)

q = 0
i = 0
reg["a"] = 7


def change_line(oldLine):
    if oldLine.startswith("jnz"):
        return "cpy " + oldLine[4:]
    if oldLine.startswith("cpy"):
        return "jnz " + oldLine[4:]
    if oldLine.startswith("inc"):
        return "dec " + oldLine[4:]
    if oldLine[:3] in ["dec", "tgl"]:
        return "inc " + oldLine[4:]


while i < len(f):
    q += 1
    line = f[i]
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
            if l in reg:
                check = reg[l]
        if check != 0:
            try:
                d = int(d)
            except:
                d = reg[d]
            i += int(d)
            continue
    elif line.startswith("tgl"):
        _, d = line.split()
        check = None
        try:
            check = int(d)
        except:
            if d not in reg:
                check = 0
            check = reg[d]
        if check != 0:
            f[(i + check) % len(f)] = change_line(f[(i + check) % len(f)])
    i += 1
print(reg["a"])

print(85 * 92 + math.factorial(12))

