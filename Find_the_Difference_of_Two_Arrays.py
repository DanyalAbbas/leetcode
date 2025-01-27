nums1 = [1,2,3]
nums2 = [2,4,6]

def foo(nums1 : list[int], nums2 : list[int]) -> list[list[int]]:
    n1 = set(nums1)
    n2 = set(nums2)
    return [list(n1 - n2),list(n2 - n1)]


print(foo(nums1, nums2))