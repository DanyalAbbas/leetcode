num = 11891

def foo(num : int) -> int:
    tempMax = str(num)
    tempMin = str(num)
    for i in tempMax:
        if i != "9":
            tempMax = tempMax.replace(i, "9")
            break
    
    for i in tempMin:
        if i != "0":
            tempMin = tempMin.replace(i, "0")
            break
    print(tempMax, tempMin)

    return int(tempMax) - int(tempMin)

print(foo(num))
