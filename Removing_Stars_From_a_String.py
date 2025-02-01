s = "*leet**cod*e"

def foo(s : str) -> str:
    NewString = []
    for i in range(len(s)):
        if s[i] == "*":
            if i > 0:
                NewString.pop()
            continue
        else:
            NewString.append(s[i])
    return "".join(NewString)

print(foo(s))