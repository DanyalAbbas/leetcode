s = "221"

def foo(s : str) -> str:
    l = list(s)
    temp = []
    for i in l:
        if l.count(i) == int(i):
            if i not in temp:
                temp.append(i)
        else:
            if temp:
                temp.pop()

    return "".join(temp) if len(temp) == 2 else "" 
            



print(foo(s))
            