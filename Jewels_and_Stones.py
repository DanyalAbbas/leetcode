jewels = "aA"
stones = "aAAbbbb"

def foo(jewels : str, stones : str) -> int:
    n = 0
    for i in stones:
        if i in set(jewels):
            n += 1

    return n

print(foo(jewels, stones))