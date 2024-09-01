s = "aab"


def foo(s : str):
    longest = 0
    temp = ""
    for i in s:
        if i not in temp:
            temp += i
            longest = max(longest, len(temp))
        else:
            temp += i
            temp = temp[temp.index(i)+1::]
    return longest
        

print(foo(s))
     