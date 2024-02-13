num = 0

def foo(num : int):
    plus = 0
    for i in range(10):
        add = [i for i in str(num)]
        for j in add:
            plus += int(j)
        if len(str(plus)) == 1:
            return plus
        num = plus
        plus = 0
        add.clear()
    return 0

print(foo(num))