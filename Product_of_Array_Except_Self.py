import math
nums = [1,3,2,4,4,4,4,4,4]

def foo(nums : list[int]) -> list[int]:
    Answer = []
    for i in range(len(nums)):
        nums_copy = nums[:]
        nums_copy.pop(i)
        Answer.append(math.prod(nums_copy))
    return Answer

nums.remove(4)

print(sorted(nums, reverse= True))
print(foo(nums))