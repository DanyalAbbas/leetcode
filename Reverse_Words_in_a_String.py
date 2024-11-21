s = "  hello world  "

def foo(s : str) -> str:
    s = s.rstrip(" ")
    s = s.lstrip(" ")
    return " ".join(s.split()[::-1])

print(foo(s))
    