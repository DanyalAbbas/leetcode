s = "abc"

def foo(s : str) -> str:
    stack = []

    for i in range(len(s)):
        if s[i].isdigit():
           stack.pop()
        else:
            stack.append(s[i])

    return ''.join(stack)

print(foo(s))