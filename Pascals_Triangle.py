numRows = 5

def foo(numRows : int) -> list[list[int]]:
    pascal_list = []
    for i in range(1, numRows+1):
        l = []
        coef = 1
        for j in range(1, i+1):
            l.append(coef)
            coef  = coef * (i-j)//j
        pascal_list.append(l)

    return pascal_list

print(foo(numRows))

    