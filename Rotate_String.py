s = "abcde"
goal = "abced"

def foo(s : str, goal : str):
    l = list(s)
    for i in l:
        l.append(l.pop(0))
        test = "".join(l)
        if test == goal:
            return True
    return False


print(foo(s,goal))