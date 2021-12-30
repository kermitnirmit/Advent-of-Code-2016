from collections import defaultdict
f = open("input.txt").read().strip().split("\n")

qwer = []
# print(len(f[:2]))
for i in range(8):
    qwer.append(defaultdict(int))
for line in f:
    print(line)
    for i in range(8):
        qwer[i][line[i]] += 1
print(qwer)
pw = ""
pw2 = ""
for i in range(8):
    m = max(qwer[i].values())
    q = min(qwer[i].values())
    for k,v in qwer[i].items():
        if v == q:
            pw2 += k
        if v == m:
            pw += k
    # pw += qwer[i].values()

print(pw)
print(pw2)
