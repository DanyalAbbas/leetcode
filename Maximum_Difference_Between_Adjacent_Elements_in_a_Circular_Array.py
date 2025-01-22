nums = [1,2,4]

def foo(nums : list[int]) -> int:
    MaximumVal = -20000000
    for i in range(len(nums)):
        if len(nums)-1 == i:
            MaximumVal = max(abs(nums[i] - nums[0]), MaximumVal)
            break
        MaximumVal = max(abs(nums[i+1] - nums[i]), MaximumVal)
    return MaximumVal



print(foo(nums))