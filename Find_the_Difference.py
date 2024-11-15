s = "abcd"
t = "abcde"

def foo(s : str, t : str) -> str:
    ACSII_value = sum(ord(i) for i in t)
    ACSII_value -= sum(ord(i) for i in s)
    return chr(ACSII_value)

print(foo(s,t))