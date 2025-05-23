nums = [1,2,3,1]

def foo(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

print(foo(nums))