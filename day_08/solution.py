f = open("input.txt").read().strip().split("\n")
from parse import parse

points = set()

for line in f:
    print(len(points))
    if line[:4] == "rect":
        # rect 9x1
        w, h = parse("rect {:d}x{:d}", line).fixed
        print("new points, ", w, h)
        for i in range(w):
            for j in range(h):
                points.add((i, j))
    else:
        axis, _, index, count = parse("rotate {} {}={:d} by {:d}", line).fixed
        print(axis, _, index, count)
        if axis == "column":
            points = set((x,y) if x != index else (x, (y + count) % 6) for x,y in points)
        else:
            points = set((x, y) if y != index else ((x + count) % 50, y) for x, y in points)
    print(points)
    # input("continue")
print(len(points))


for i in range(6):
    builder = ""
    for j in range(50):
        if (j,i) in points:
            builder += "#"
        else:
            builder += " "
    print(builder)
