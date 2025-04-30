s = "abcdefg"
k = 2

def foo(s : str, k : int):
    temp = ""
    n = 0
    for i in range(0,len(s),k):
        if n % 2*k == 0:
            temp += s[i:i+k][::-1]
        else:
            temp += s[i:i+k]
        n += 1
    return temp

print(foo(s,k))