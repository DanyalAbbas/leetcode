pattern = "deadbeef"
s = "d e a d b e e f"

def foo(pattern : str, s : str):
    d = {}
    count = 0

    if len(s.split()) == len(pattern):
        pass
    else:
        return False

    for i in pattern:
        if i not in d.values() and s.split()[count] not in d.keys():
            d[s.split()[count]] = i
        count += 1
    for pos, i in enumerate(s.split()):
        if d.get(i) == pattern[pos]:
            if pos == pattern[pos]:
                pass
        else:
            return False
    return True
       
print(foo(pattern,s))
