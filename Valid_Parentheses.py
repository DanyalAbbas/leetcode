s = r"()[]{"


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
        elif len(temp) >= 1 and BracketsDict[i] == temp[-1]:
            temp.pop()
        else:
            return False

    return not len(temp)

print(foo(s))