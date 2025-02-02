n = 7

def foo(n : int) -> int:
    SummedValue = 0
    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            SummedValue += i
    return SummedValue

print(foo(n)) 