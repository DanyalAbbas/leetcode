nums = [-2,1,-3,4,-1,2,1,-5,4]

def foo(nums : list[int]):
    minimumNum = -10000000
    num = 0
    for i in nums:
        num += i
        minimumNum = max(minimumNum, num)
        if num < 0: num=0
    return minimumNum


print(foo(nums))