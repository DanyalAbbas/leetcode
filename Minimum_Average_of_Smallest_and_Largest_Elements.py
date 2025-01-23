nums = [7,8,3,4,15,13,4,1]


def foo(nums: list[int]) -> float:
    averages = []
    for i in range(len(nums)//2):
        averages.append((min(nums)+max(nums))/2)
        nums.remove(min(nums))
        nums.remove(max(nums))
    return min(averages)

print(foo(nums))
