nums = [1,2,3,4]
k = 5

def foo(nums : list[int], k : int) -> int:
    Count = 0
    nums = sorted(nums)
    LeftPointer = 0
    RightPointer = len(nums) - 1
    while LeftPointer < RightPointer:
        if (nums[LeftPointer] + nums[RightPointer] == k):
            LeftPointer += 1
            RightPointer -= 1
            Count += 1
        elif (nums[LeftPointer] + nums[RightPointer] < k):
            LeftPointer += 1
        else:
            RightPointer -= 1
    return Count


print(foo(nums, k))