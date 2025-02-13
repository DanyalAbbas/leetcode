num = 9669

def foo(num : int) -> int:
    hehe = str(num).replace("6", "9", 1)
    return int(hehe)


print(foo(num))
