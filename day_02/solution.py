f = open("input.txt").read().strip().split('\n')
# f = open("test.txt").read().strip().split('\n')


#   1   2   3
#   4   5   6
#   7   8   9
#

# an up subtracts 3 if > 3 it can else doesn't do anything
# a down adds 3 if < 7 else it doesn't do anything
# a left subtracts 1 unless it's 1/4/7
# a right adds 1 unless its 369
curr = 5
final = ""
for line in f:
    for char in line:
        if char == "U" and curr > 3:
            curr -= 3
        if char == "D" and curr < 7:
            curr += 3
        if char == "L" and curr not in [1,4,7]:
            curr -= 1
        if char == "R" and curr not in [3,6,9]:
            curr += 1
    final += str(curr)

print(final)

# p2
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

# an up subtracts 4 if 6,7,8 10 11 12 | 2 if 3 or 13 or does nothing if 5 ,9
# a down adds 4 if 2,3,4,6,7,8 | 2 if 1 or 11 or does nothing if 5,9
# a left subtracts 1 unless 1,2,5,10,13
# a right adds 1 unless 1,4,9,12,13

curr = 5
table = [None, "1","2","3","4","5","6","7","8","9","A","B","C","D"]
final = ""
for line in f:
    for char in line:
        if char == "U" and curr not in [1,2,4,5,9]:
            if curr in [6,7,8,10,11,12]:
                curr -= 4
            else:
                curr -= 2
            # curr -= 3
        if char == "D" and curr not in [5,10,13,12,9]:
            if curr in [2,3,4,6,7,8]:
                curr += 4
            else:
                curr += 2
        if char == "L" and curr not in [1,2,5,10,13]:
            curr -= 1
        if char == "R" and curr not in [1,4,9,12,13]:
            curr += 1
    final += table[curr]
print(final)