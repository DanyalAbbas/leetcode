nums = [-1,-1,0,0,-1,-1]

def foo(nums : list[int]) -> int:
    Value = 0
    Pivot = -1
    for i in range(len(nums)):
        if i == 0:
            Value = 0
        else:
            Value = sum(nums[:i:])
        if Value == sum(nums[i+1::]):
            return i
    return Pivot

print(foo(nums))