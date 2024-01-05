nums = [3,2,3]
target = 6
p = []
for pos1,i in enumerate(nums):
    for pos2, j in enumerate(nums[1::]):
            if i + j == target:
                if pos1 != pos2+1:
                    p.append(pos1)
                    p.append(pos2+1)
                if len(p) == 2:
                    nums.clear()
                break
print(p)