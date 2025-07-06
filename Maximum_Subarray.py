nums = [-2,1,-3,4,-1,2,1,-5,4]

def foo(nums : list[int]):
    ans = -10000000
    num = 0
    for i in nums:
        num += i
        ans = max(ans, num)
        if num < 0: num=0
    return ans


print(foo(nums))