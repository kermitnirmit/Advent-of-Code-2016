import re
import hashlib



base_string = "ihaygndm"
# base_string = "abc"

seen_before = {}
def generate_hash(v, stretch):
    if (v, stretch) in seen_before:
        return seen_before[(v,stretch)]
    hsh = hashlib.md5((base_string + str(v)).encode()).hexdigest()
    if stretch:
        for _ in range(2016):
            hsh = hashlib.md5(hsh.encode()).hexdigest()
    seen_before[(v,stretch)] = hsh
    return hsh



def check_for_five(a, c, p2):
    for i in range(a+1, a+1002):
        check = generate_hash(i, p2)
        if c * 5 in check:
            return True
    return False




def solve(p2=False):
    valids = []
    i = 0
    while len(valids) < 64:
        check = generate_hash(i, p2)

        char_to_check = re.findall(r"([a-z\d])\1\1", check)

        if len(char_to_check) >= 1:
            has_it = check_for_five(i, char_to_check[0], p2)
            if has_it:
                valids.append(i)
                # print(valids, i, char_to_check)

        i += 1
    return valids[-1]

print(solve())
print(solve(True))