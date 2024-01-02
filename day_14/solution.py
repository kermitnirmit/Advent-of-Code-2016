import re
from collections import Counter, deque
import hashlib

from day_13.utils import add_tuples

print(hashlib.md5(b"abc18").hexdigest())

base_string = "abc"

i = 18
while True:
    s = base_string + str(i)

    check = hashlib.md5(s.encode()).hexdigest()
    i+=1

    char_to_check = re.findall(r"([a-z\d])\1\1", check)

    print(char_to_check[0])

    print(check)
    input("contiinue")