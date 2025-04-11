height = [4,2,3]

def foo(height : list[int]) -> int:
    WaterAmount = 0
    start = 0
    length = len(height)


    for i in range(length):
        if height[i] != 0:
            start = i
            break
    maximum = max(height) + 1
    height.append(maximum)
    height.insert(start, maximum)
    
    for i in range(start+1, len(height)):
        if height[i] >= height[start]:
            WaterAmount += (min(height[start], height[i])*(i-start)) -  sum(height[start:i])
            start = i

    return (length*(maximum-1)) - WaterAmount 

print(foo(height))
        
    
