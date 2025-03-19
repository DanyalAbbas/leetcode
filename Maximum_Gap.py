nums = [3,6,9,1]

def foo(nums : list[int]) -> int:
    if len(nums) <= 1:
        return 0
    nums.sort()
    for i in range(1, len(nums)):
        nums[i-1] = nums[i] - nums[i-1]
    return max(nums[:-1])


print(foo(nums))
