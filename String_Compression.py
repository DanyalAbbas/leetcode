chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

def foo(chars : list[str]) -> int:
    s = []
    temp = ""
    for i in chars:
        if len(temp) == 0:
            temp += i
            continue
        if i in temp:
            temp += i
        else:
            s.append(temp[0])
            if len(temp) > 1:
                if len(str(len(temp))) > 1:
                    for j in str(len(temp)):
                        s.append(j)
                else:
                    s.append(str(len(temp)))
            temp = i

    s.append(temp[0])
    if len(temp) > 1:
        if len(str(len(temp))) > 1:
            for j in str(len(temp)):
                s.append(j)
        else:
            s.append(str(len(temp)))
    
    chars.clear()
    for i in s:
        chars.append(i)

    print(chars)
    return len(chars)
        


print(foo(chars))