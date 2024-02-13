s = "0P"

def foo(s : str):
    j = ""
    for i in s:
        if i.isalpha():
            j += i.lower()
        elif i.isnumeric():
            j += str(i)
    if j[::-1] == j:
        return True
    else:
        return False
    
print(foo(s))
