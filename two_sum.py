nums = [2,7,11,15]
target = 9

def foo(nums : list[int], target : int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            elif nums[i] + nums[j] == target:
                return [i,j]


print(foo(nums, target))