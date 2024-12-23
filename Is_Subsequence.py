s = "aaaaaa"
t = "bbaaaa"

def foo(s : str, t : str) -> bool:
    index = 0
    i = 0
    while i < len(s):
        t = t[index::]
        print(t)
        if t.find(s[i]) >= 0:
            index = t.find(s[i]) +1
            i += 1
        else:
            return False
    return i == len(s)
        

    


print(foo(s,t))
# print(t.find("j"))