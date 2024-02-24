n = 27

def foo(n : int):
    for i in range(100):
        if 3**i == n:
            return True
    return False

print(foo(n))