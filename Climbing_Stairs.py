n = 5

def foo(n):
    l = [1,1]
    for i in range(1,n):
        l.append(l[i]+l[i-1])
    return l[n]

print(foo(n))



