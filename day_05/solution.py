import hashlib

pw = ""
start = "uqwqemis"
# start = "abc"

arr = [None] * 8
# setindexes = [0] * 8
i = 0
index = 0
otheri = 0
# print(hashlib.md5("abc3231929".encode()).hexdigest())

#
while i < 8 or otheri < 8:
    hashy = hashlib.md5((start + str(index)).encode())
    care = hashy.hexdigest()
    if care[:5] == "00000":
        if care[5] in "01234567" and arr[int(care[5])] is None:
            arr[int(care[5])] = care[6]
            otheri += 1
            print(arr)
        if i < 8:
            pw += hashy.hexdigest()[5]
            print(pw)
            i += 1
    index += 1
print(pw)
print("".join(arr))
