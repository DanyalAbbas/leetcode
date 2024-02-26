s = "rat"
t = "car"

def foo(s : str, t : str):
    if len(s) == len(t):
        for i in set(s):
            if t.count(i) == s.count(i):
                pass
            else:
                return False
        return True


print(foo(s,t))