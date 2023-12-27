from collections import defaultdict
from parse import parse
f = open("input.txt").read().strip().splitlines()

bots = defaultdict(list)
outputs = defaultdict(int)
insts = []
for line in f:
    if line.startswith("value"):
        left, right = line.split(" goes to bot ")
        val, bot = int(left[6:]), int(right)
        bots[bot].append(val)
        assert len(bots[bot]) <= 2
    else:
        everything = parse("bot {:d} gives low to {} {:d} and high to {} {:d}", line)
        insts.append(everything)
while True:
    twos = []
    for k, v in bots.items():
        if len(v) == 2:
            twos.append(k)
            if min(v) == 17 and max(v) == 61:
                print(k)
    if len(twos) == 0:
        break

    for two in twos:
        for inst in insts:
            if inst[0] == two:
                low = min(bots[two])
                hi = max(bots[two])
                if inst[1] == "bot":
                    bots[inst[2]].append(low)
                    assert len(bots[inst[2]]) <= 2
                if inst[1] == "output":
                    outputs[inst[2]] = low
                if inst[3] == "bot":
                    bots[inst[4]].append(hi)
                    assert len(bots[inst[4]]) <= 2
                if inst[3] == "output":
                    outputs[inst[4]] = hi
                bots[two].clear()

print(outputs[0] * outputs[1] * outputs[2])