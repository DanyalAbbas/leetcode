n = 10

def foo(n : int) -> int:
    if n < 3: return 0
    l = [True] * n
    l[0] = l[1] = False
    m = 2
    while m*m < n:
        if l[m]:
            for i in range(m * m, n,  m):
               l[i] = False
        
        m += 1 if m == 2 else 2
    
    return sum(l)


print(foo(n))
    

