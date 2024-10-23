rowIndex = 3

def foo(rowIndex : int) -> list[int]:
    pascal_list = []
    for i in range(1, rowIndex+2):
        l = []
        coef = 1
        for j in range(1, i+1):
            l.append(coef)
            coef  = coef * (i-j)//j
        pascal_list.append(l)

    return pascal_list[rowIndex]

print(foo(rowIndex))