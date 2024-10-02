nums = [14,4,6,-1,10,9,-8,7,-13,14,-13,-11,-8,-9,11,14,-8,-14,-13,7,-10,-15,-13,-11,-11,11,14,13,2,-14,1,-7,-2,14,-1,-15,9,7,-1,3,6,1,7,5,-1,-5,4,-2,-4,-1,-9,-7,-1,-7,-11,3,12,10,-7,-1,12,1,8,-13,1,14,9,-13,6,-7,-3,-11,2,-11,10,-14,-1,-9,0,2,5,6,3,-11,6,7,0,3,3,0,-12,-8,-13,3,-14,-5,2,10,-11,-14,-12,1,-10,5,5,7,-1,11,14,6,-10,-4,-3,8,-7,10,1,8,-1,-11,-15,-6,-12,-13,12,-11]

def foo(nums : list[int]) -> list:
    threesum = []
    for pos1, i in enumerate(nums):
        for pos2, j in enumerate(nums[1::]):
            for pos3, k in enumerate(nums[2::]):
                if (i+j+k == 0) and ((pos1 != pos2+1 and pos1 != pos3+2) and (pos2+1 != pos3+2)) and (sorted([i,j,k]) not in [sorted(i) for i in threesum]):
                    threesum.append([i,j,k])
    return threesum


def bar(nums : list[int]):
    nums.sort()
    threesum = set()
    for i in range(len(nums) - 2):
        firstNum = nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            secondNum  = nums[left]
            thirdNum = nums[right]

            potentialSum = firstNum + secondNum + thirdNum 
            if potentialSum > 0:
                right -= 1
            elif potentialSum < 0:
                left += 1
            else:
                threesum.add((firstNum , secondNum ,thirdNum))
                left += 1
                right -= 1
    return threesum


print(foo(nums)) # slow
print(bar(nums)) # fast

l = [[1,-1,0]]
if [-1,0,1] in l:
    print("hey")
# print(sorted([1,-1,0]) == sorted([-1,0,1]))