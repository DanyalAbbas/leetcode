nums = [0,0,0,0,0]

def foo(nums : list[int]) -> int:
    i = 0
    while i < len(nums):
        if nums.count(nums[i]) > 2:
            nums.pop(i)
            i-=1
        i += 1
    
    return len(nums)


print(foo(nums))