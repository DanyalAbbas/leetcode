nums = [1,1,2]

def foo(nums : list[int]) -> int:
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k


print(foo(nums))