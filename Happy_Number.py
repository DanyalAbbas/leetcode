n = 2

def foo(n : int):
    plus = 0
    for i in range(10):
        add = [i for i in str(n)]
        for i in add:
            plus += int(i)**2
        if plus == 1:
            return True
        else:
            add.clear()
            n = plus
            plus = 0
    return False

        

print(foo(n))