
f = open("input.txt").read().strip().split(", ")

print(f)


x, y = 0 , 0
# face North

locs = set()

found = False

facing = 0
dirs = "nesw"
for a in f:
    newy = y
    newx = x
    dir = a[0]
    steps = int(a[1:])
    locs_in_between = []
    if dir == "L":
        facing = (facing - 1) % 4
    if dir == "R":
        facing = (facing + 1) % 4
    if facing % 2 == 0: # north or south
        if facing == 0:
            newy += steps
        else:
            newy -= steps
    else:
        if facing == 1:
            newx += steps
        else:
            newx -= steps
    for q in range(min(x, newx), max(x, newx) + 1):
        for w in range(min(y, newy), max(y, newy) + 1):
            if (q,w) != (x,y):
                locs_in_between.append((q,w))
    y = newy
    x = newx
    # print(a)
    # print(locs_in_between)
    # input("continue")
    for l in locs_in_between:
        if l in locs:
            if not found:
                print((abs(l[0]) + abs(l[1])))
            found = True
            break
        else:
            locs.add((l[0], l[1]))

print(abs(x) + abs(y))

