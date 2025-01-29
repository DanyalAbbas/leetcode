grid = [[9,1,7],[8,9,2],[3,4,6]]

def foo(grid : list[list[int]]) -> list[int]:
    MaxNumber = len(grid)**2
    NewList = []
    RepeatedValue = 0
    MissingValue = 0
    for i in grid:
        NewList += i
    
    for i in range(MaxNumber + 1):
        if NewList.count(i) > 1:
            RepeatedValue = i
        elif NewList.count(i) == 0:
            MissingValue = i
    
    return [RepeatedValue, MissingValue]

        

print(foo(grid))