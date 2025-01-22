nums = [2,3,1]

def foo(nums : list[int]) -> int:
    tot = 0
    for pos, i in enumerate(nums):
        tot += sum(nums[max(0,pos-i):pos+1])
    return tot

print(foo(nums))