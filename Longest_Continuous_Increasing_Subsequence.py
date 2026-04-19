nums = [1,3,5,4,2,3,4,5]


def foo(nums : list[int]) -> int:
    maxSequence = 1
    temp = 1
    prev = nums[0]
    for i in nums[1::]:
        if i > prev:
            temp += 1
        else:
            maxSequence = max(maxSequence,temp)
            temp = 1 
        prev = i

    maxSequence = max(temp, maxSequence)
    return maxSequence

print(foo(nums))