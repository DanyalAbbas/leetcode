height = [75,21,3,152,13,107,163,166,32,160,41,131,7,67,56,5,153,176,29,139,61,149,176,142,64,75,170,156,73,48,148,101,70,103,53,83,11,168,1,195,81,43,126,88,62,134,45,167,63,26,107,124,128,83,67,192,158,189,149,184,37,49,85,107,152,90,143,115,58,144,62,139,139,189,180,153,75,177,121,138,4,28,15,132,63,82,124,174,23,25,110,60,74,147,120,179,37,63,94,47]

def foo(height : list[int]) -> int:
    Maximum_Water = 0
    for pos1, i in enumerate(height):
        for pos2, j in enumerate(height[::-1]):
            Potential_Max_Water = min(i,j)*len(height[pos1:len(height)-1 -pos2])
            Maximum_Water = max(Maximum_Water,Potential_Max_Water)
            # print(height[pos1:len(height) - pos2])
            # print("max ", Potential_Max_Water)

    return Maximum_Water

def bar(height : list[int]) -> int:
    Maximum_Water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        i = height[left]
        j = height[right]

        Potential_Max_Water = min(i,j) * (right-left)
        Maximum_Water = max(Maximum_Water,Potential_Max_Water)

        if i < j:
            left += 1
        else:
            right -= 1
    return Maximum_Water



print(foo(height))
print(bar(height))
