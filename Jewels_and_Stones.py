jewels = "aA"
stones = "aAAbbbb"

def foo(jewels : str, stones : str) -> int:
    # stones = str(set(stones))
    n = 0
    for i in stones:
        if i in jewels:
            n += 1

    return n

print(foo(jewels, stones))