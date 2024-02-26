nums = [2,2,1]

def foo(nums : list):
    for i in nums:
        if nums.count(i) == 1:
            return i

print(foo(nums))