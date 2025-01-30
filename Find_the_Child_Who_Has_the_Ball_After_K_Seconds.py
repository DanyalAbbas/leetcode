n = 5
k = 6

def foo(n : int, k : int) -> int:
    CurrentChild = 0
    Rotation = True
    i = 0
    while i < k:
        if CurrentChild == n - 1:
            Rotation = False
        elif CurrentChild == 0:
            Rotation = True
        CurrentChild += 1 if Rotation else -1
        i += 1
    return CurrentChild


print(foo(n, k))