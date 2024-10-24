nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def foo(nums1 : list[int], m : int, nums2 : list[int], n : int) -> list[int]:

    while len(nums1) > m:
            nums1.remove(0)
    while len(nums2) > n:
            nums2.remove(0)

    NewNums = nums1 + nums2
    NewNums.sort()
    nums1.clear()
    for i in range(len(NewNums)):
        nums1.append(NewNums[i])



foo(nums1, m, nums2, n)
print(nums1)