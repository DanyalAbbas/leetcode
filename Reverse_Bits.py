n = 10100101000001111010011100

def foo(n : int) -> int:
    n = str(n)[::-1]
    return int(n,2)


print(foo(n))
