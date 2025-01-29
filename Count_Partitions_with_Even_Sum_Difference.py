nums = [2,4,6,8]

def foo(nums : list[int]) -> int:
    Length = len(nums)
    NoOfPartitions = 0
    for i in range(Length-1):
        if (sum(nums[0:i+1]) - sum(nums[i+1:Length])) % 2 == 0:
            NoOfPartitions += 1
    
    return NoOfPartitions


print(foo(nums))