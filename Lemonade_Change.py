bills = [5,5,5,10,5,5,10,20,20,20]

def foo(bills : list):
    change5, change10 = 0 , 0
    for i in bills:
        if i == 5:
            change5 += 1
        elif i == 10:
            if change5:
                change5 -= 1
                change10 += 1
            else:
                return False
        else:
            if change5 and change10:
                change5 -= 1
                change10 -= 1
            elif change5 >=3:
                change5 -= 3
            else:
                return False
    return True
            


print(foo(bills))