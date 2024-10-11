import math
num = 28

def foo(num : int) -> bool:
    if num < 5:
            return False
        
    add = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            add += i + num//i
    return add == num

print(foo(num))
