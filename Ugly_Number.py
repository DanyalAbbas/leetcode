n = 12

def foo(n : int) -> bool:
    factors = [2,3,5]

    Number = n
    UglyNumber = 1
    factor = 2
    
    i = 0
    while Number > i:
        if factor > 5:
            break
        if UglyNumber == Number:
            return True
        if n % factor == 0 and factor in factors:
            n = n//factor
            UglyNumber *= factor
        else:
            factor +=1
        i += 1
    
    return True if Number <=2 and Number > 0 else False

            

print(foo(n))