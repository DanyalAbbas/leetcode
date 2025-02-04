import math
coordinates = [[1,-8],[2,-3],[1,2]]

def foo(coordinates : list[list[int]]) -> bool:
    if (coordinates[1][0] - coordinates[0][0]) == 0:
        Slope = "inf"
    else:
        Slope = abs((coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]))
    
    for i in range(2,len(coordinates)):
        if (coordinates[i][0] - coordinates[i-1][0]) == 0:
            Temp_Slope = "inf"
        else:
            Temp_Slope = abs((coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0]))
        print(i)
        print(Slope, Temp_Slope)
        if (Slope != Temp_Slope):
            return False
    return True

print(foo(coordinates))