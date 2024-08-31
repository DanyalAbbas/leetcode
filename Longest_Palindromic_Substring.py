s = "babad"

def foo(s : str):
    palin = ""
    for i in range(len(s)):
        for j in range(i, len(s) +1):
            k = s[i:j]
            if k == k[::-1] and len(palin) < len(k):
                palin = s[i:j]
    return palin

print(foo(s))