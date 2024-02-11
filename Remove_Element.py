nums = [0,1,2,2,3,0,4,2]
val = 2
n = nums.copy()
for pos,i in enumerate(n):
    if i == val:
        nums.remove(i)

# nums[:] = [i for i in nums if i!= val]

print(nums)