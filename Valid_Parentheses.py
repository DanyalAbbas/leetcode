s = r"()[]{}"


def foo(s : str):
    BracketsDict = {")" : "(",
                    "]" : "[",
                    "}" : "{"}

    temp = []
    if ("(" or "[" or "{") not in s and len(s) <= 1:
        return False
    for i in s:
        if i in BracketsDict.values():
            temp.append(i)
        elif BracketsDict[i] == temp[-1]:
            temp.pop()

    return True if len(temp) == 0 else False

print(foo(s))