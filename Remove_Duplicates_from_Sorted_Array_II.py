nums = [1,1,1,2,2,3]

def foo(nums : list[int]) -> int:
    i = 0
    counter = 1
    while i < len(nums)-1:
        CurrValue = nums[i]
        if nums[i+1] == CurrValue:
            if counter > 1:
                nums.pop(i)
                i -= 1
            counter += 1
        if nums[i+1] != CurrValue:
            counter = 1
        i += 1
    
    return len(nums)


print(foo(nums))