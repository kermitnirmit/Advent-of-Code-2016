def solve(p2=False):
    f = open("input.txt").read().splitlines()
    f = f[0]
    c = sum(1 if x == "." else 0 for x in f)
    m = 400000 if p2 else 40
    m -= 1
    for i in range(m):
        n = ""
        for index, char in enumerate(f):
            if 1 <= index <= len(f) - 2:
                q = f[index - 1:index + 2]
            else:
                if index == 0:
                    q = "." + f[:2]
                else:
                    q = f[-2:] + "."
            # Its left and center tiles are traps, but its right tile is not.
            # Its center and right tiles are traps, but its left tile is not.
            # Only its left tile is a trap.
            # Only its right tile is a trap.
            if q in ["^^.", ".^^", "^..", "..^"]:
                n += "^"
            else:
                n += "."
                c += 1
        f = n
    return c


print(solve())  # 1987
print(solve(True))  # 19984714
