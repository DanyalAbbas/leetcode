nums = [2,1]
k = 1

def foo(nums : list[int], k : int) -> int:
    GoodSum = 0
    length = len(nums)
    for i in range(length):
        if (i-k) >= 0 and (i+k) < length:
            if nums[i] > nums[i-k] and nums[i] > nums[i+k]:
                GoodSum += nums[i]
                
        elif (i+k) < length and (i-k) < 0:
            if nums[i] > nums[i+k]:
                GoodSum += nums[i]
                
        elif (i+k) >= length and (i-k) >= 0:
            if nums[i] > nums[i-k]:
                GoodSum += nums[i]
                
        else:
            GoodSum += nums[i]   
    return GoodSum
    
    
print(foo(nums,k))