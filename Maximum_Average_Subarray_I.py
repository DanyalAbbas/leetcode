nums = [1,12,-5,-6,50,3]
k = 4

def foo(nums : list[int], k : int) -> float:
    i = k-1
    maximum = sum(nums[0:k])
    smt = sum(nums[0:k])/k
    while i < len(nums) - 1:
        maximum -= nums[i-(k-1)]
        i += 1
        maximum += nums[i]
        smt = max(smt,maximum/k)
    return smt

print(foo(nums,k))
