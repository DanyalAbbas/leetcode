s = "leetcode"

def foo(s : str) -> int:
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    earliest = 100000000
    for key, value in d.items():
        if value == 1:
            earliest = min(s.index(key), earliest)


    return -1 if earliest == 100000000 else earliest


def foo(s : str) -> int:
    used = ""
    for pos, i in enumerate(s):
        if s.find(i, pos+1) == -1 and i not in used:
            return pos
        used += i
    return -1



print(foo(s))