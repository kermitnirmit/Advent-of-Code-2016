f = open("input.txt").read().strip().split("\n")
# f = open("test.txt").read().strip().split("\n")
from itertools import permutations

count = 0
for line in f:
    valid = True
    q = line.split(" ")
    q = list(map(int, list(filter(lambda x: len(x) > 0, q))))
    # print(q)

    # input("continue")
    for a, b, c in permutations(q, r=3):
        if a + b <= c:
            valid = False
            break
    if valid:
        count += 1
print(count)


count = 0
firsts = []
seconds = []
thirds = []
for line in f:
    valid = True
    q = line.split(" ")
    q = list(map(int, list(filter(lambda x: len(x) > 0, q))))
    firsts.append(q[0])
    seconds.append(q[1])
    thirds.append(q[2])

qwer = firsts + seconds + thirds
qwer = [qwer[i:i + 3] for i in range(0, len(qwer), 3)]
print(qwer)

for t in qwer:
    valid = True
    for a, b, c in permutations(t, r=3):
        if a + b <= c:
            valid = False
            break
    # print(list(permutations(t, r=3)), valid)
    if valid:
        count += 1
print(count)