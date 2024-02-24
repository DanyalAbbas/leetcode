s = "papap"
t = "title"

def foo(s : str, t : str):
    d1 = {}
    d2 = {}
    for i in range(len(s)):
        s1 = s[i]
        s2 = t[i]
        if s1 in d1 and d1[s1] != s2 or s2 in d2 and d2[s2] != s1:
            return False

        d1[s1] = s2
        d2[s2] = s1

    return True
            


print(foo(s,t))