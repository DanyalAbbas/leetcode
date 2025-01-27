import math
nums = [-1,1,0,-3,3]

def foo(nums : list[int]) -> list[int]:
    numscopy = nums[:]
    ZeroCount = nums.count(0)
    for i in range(ZeroCount):
        nums.remove(0)
    AllProduct = math.prod(nums)
    ProductedValues = []
    if ZeroCount > 1:
        return [0] * len(numscopy)
    elif ZeroCount == 0:
        for i in range(len(nums)):
            ProductedValues.append(int(AllProduct/nums[i]))
    elif ZeroCount == 1:
        ProductedValues = [0] *  len(numscopy)
        ProductedValues[numscopy.index(0)] = AllProduct

    return ProductedValues

print(foo(nums))
    