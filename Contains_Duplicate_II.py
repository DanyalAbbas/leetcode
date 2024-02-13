nums = [1, 2, 3, 1]
k = 3


def foo(nums, k):
    num_index = {}
    
    for pos, i in enumerate(nums):
        if i in num_index and pos - num_index[i] <= k:
            return True
        num_index[i] = pos
    
    return False

print(foo(nums,k))
