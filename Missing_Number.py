nums = [3,0,1]

def foo(nums : list):
    for i in range(len(nums)):
        if i not in nums:
            return i
    return len(nums)


print(foo(nums))