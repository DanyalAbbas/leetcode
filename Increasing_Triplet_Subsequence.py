nums = [1,5,0,4,1,3]

def foo(nums : list[int]) -> bool:
    min1 = float('inf')
    min2 = float('inf')
    for n in nums:
        if n <= min1:
            min1 = n  # Update first minimum
        elif n <= min2:
            min2 = n  # Update second minimum
        else:
            return True  # Found a third number greater than both
    return False  # No triplet found

print(foo(nums))




# for pos1, i in enumerate(nums):
#         for pos2, j in enumerate(nums):
#             for pos3, k in enumerate(nums):
#                 if (i < j < k) and (pos1 < pos2 < pos3):
#                     return True

#     return False