def checkabba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i+1] != s[i] and s[i+1] == s[i + 2]:
            return True
    return False

f = open("input.txt").read().strip().split("\n")
import re
c = 0
for line in f:
    goods = []
    goods.append(0)
    middles = re.finditer(r'\[.*?]', line)
    anyMiddle = False
    for m in middles:
        left, right = m.span()
        goods.append(left)
        goods.append(right)
        middle = line[m.span()[0] + 1 : m.span()[1] - 1]
        if checkabba(middle):
            anyMiddle = True
    foundabba = False
    for i, index in enumerate(goods):
        if i % 2 == 0:
            if i + 1 < len(goods):
                foundabba = foundabba or checkabba(line[index:goods[i+1]])
            else:
                foundabba = foundabba or checkabba(line[index:])
    if foundabba and not anyMiddle:
        c += 1
print(c)


c = 0
for line in f:
    goods = []
    goods.append(0)
    middles = re.finditer(r'\[.*?]', line)
    anyMiddle = False
    middlestrs = []
    for m in middles:
        left, right = m.span()
        goods.append(left)
        goods.append(right)
        middle = line[m.span()[0] + 1: m.span()[1] - 1]
        middlestrs.append(middle)
    otherstrs = []
    for i, index in enumerate(goods):
        if i % 2 == 0:
            if i + 1 < len(goods):
                otherstrs.append(line[index: goods[i+1]])
            else:
                otherstrs.append(line[index:])
    #     look in others and find the xyxs -> create a set of the corresponding yxys
    #       look in middles if that three letter seq in set
    yxys = set()
    for outside in otherstrs:
        for i in range(len(outside) - 2):
            if outside[i] == outside[i+2] and outside[i] != outside[i+1]:
                newstr = outside[i+1] + outside[i] + outside[i+1]
                yxys.add(newstr)
    foundMatch = False
    for m in middlestrs:
        for i in range(len(m) - 2):
            if m[i:i+3] in yxys:
                foundMatch = True
    if foundMatch:
        c += 1
#
print(c)