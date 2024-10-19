s = '-5-'

def foo(s : str) -> int:
    new_string = ""
    s = s.lstrip(" ")
    if not(s):
        return 0

    if (s[0] == "-" or s[0] == "+") and len(s) > 1:
        new_string += s[0]+"0" if s[0] == "-" else ""
        s = s[1::]
        
    for i in s:
        if i.isdigit():
            new_string += i
        else:
            break
    
    new_string = int(new_string if new_string else 0)

    if new_string < (-2**31):
        new_string = -2**31
    elif new_string > ((2**31) - 1):
        new_string = (2**31) - 1
        
    return new_string


print(foo(s))

