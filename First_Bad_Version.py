n = 5
bad = 4

def isBadVersion(version: int) -> bool:
    pass 

def foo(n : int) -> int:
    i = 1
    j = n
    while (i < j):
        pivot = (i+j) // 2
        if (isBadVersion(pivot)):
            j = pivot       
        else:
            i = pivot + 1
    return i
