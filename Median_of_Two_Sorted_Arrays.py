import math
nums1 = [2,2,4,4]
nums2 = [2,2,2,4,4]

def foo(nums1 : list, nums2 : list) -> float:
    new = sorted(nums1+nums2)

    i = 0
    j = len(new) -1

    median = (i+j)/2
    print(median)
    if median % 2 == 0:
        return new[int(median)]
    

    return (new[math.floor(median)] + new[math.ceil(median)])/2


print(foo(nums1, nums2))