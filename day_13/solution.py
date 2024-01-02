from collections import Counter, deque

from day_13.utils import add_tuples


# f = open("input.txt").read().strip().splitlines()

def free_space(x,y, num):
    q = x * x + 3 * x + 2 * x * y + y + y * y
    q += num

    # return bin(q)
    c = Counter(bin(q)[2:])
    # print(bin(q))
    # If the number of bits that are 1 is even, it's an open space.
    # If the number of bits that are 1 is odd, it's a wall.
    # print(c)
    if c["1"] % 2 == 0:
        return True
    else:
        return False

# he cube maze starts at 0,0 and seems to extend infinitely toward positive x and y; negative values are invalid, as
# they represent a location outside the building. You are in a small waiting area at 1,1.
dirs_2d_4 = {(0, 1), (1, 0), (0, -1), (-1, 0)}

start = (1, 1)

q = [(start, 0)]
goal = (31, 39)
goal = (7,4)
q = deque(q)

secret_num = 1364
# secret_num = 10

q = [(start, 0, [])]
goal = (39, 31)
# goal = (4,7)
q = deque(q)

v = set()
while q:
    curr, l, path = q.popleft()
    if l > 50:
        continue
    if curr in v:
        continue
    else:
        v.add(curr)
        # print(curr, path)
        for nd in dirs_2d_4:
            ni, nj = add_tuples(curr, nd)
            if 0 <= ni and 0 <= nj:
                if free_space(nj, ni, secret_num):
                    q.append(((ni, nj), l + 1, path + [curr]))
print(len(v))