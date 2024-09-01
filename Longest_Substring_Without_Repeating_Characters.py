s = "aabaab!bb"

def foo(s : str):
    longest = 0
    temp = ""
    for i in range(len(s)):
        print(temp)
        if s[i] not in temp:
            temp += s[i]
        else:
            temp = temp[temp.find(s[i]):i:]
        longest = max(longest, len(temp))
    return longest
        

print(foo(s))
     