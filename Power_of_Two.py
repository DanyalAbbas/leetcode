n = 3

def foo(n : int):
    for i in range(50):
        if 2**i == n:
            return True
    return False

print(foo(n))