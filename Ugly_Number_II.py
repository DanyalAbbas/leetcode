n = 1000

def foo(n : int) -> int:
    # not my solution
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    t2 = t3 = t5 = 0
    k = [0] * n
    k[0] = 1
        
    for i in range(1, n):
        k[i] = min(k[t2] * 2, k[t3] * 3, k[t5] * 5)
            
        if k[i] == k[t2] * 2:
            t2 += 1
        if k[i] == k[t3] * 3:
            t3 += 1
        if k[i] == k[t5] * 5:
            t5 += 1
        
    return k[-1]

print(foo(n))

