f = open("input.txt").read().strip().split("\n")
from collections import Counter

rsum = 0
real_rooms = []
for line in f:
    q = line.split("-")
    last = q[-1]
    l, r = last.split("[")
    r = r[:-1]

    q = "".join(q[:-1])
    c = Counter(q)

    d = dict(sorted((dict(sorted(c.items(), key=lambda item: item[0]))).items(), key=lambda item: item[1], reverse=True))


    # print(d)
    print("".join(list(d.keys())[:5]))
    if "".join(list(d.keys())[:5]) == r:
        rsum += int(l)
        real_rooms.append((q, l, r))
    # print(q)

print(rsum)
# print(real_rooms)
#
# print(ord("a"))
# print(chr(((ord("d") - ord("a")) + 101) % 26 + ord("a")))

for w, sid, _ in real_rooms:
    new_str = ""
    for char in w:
        new_str += chr(((ord(char) - ord("a")) + int(sid)) % 26 + ord("a"))
    # print(new_str, sid)
    if "north" in new_str:
        print(new_str, sid)


