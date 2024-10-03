nums = [-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38]
target = 78

def foo(nums : list, target : list):
    closest = nums[0]+nums[1]+nums[2]
    nums.sort()
    for i in range(len(nums)-2):
        FirstNum = nums[i]

        left = i+1
        right = len(nums)-1

        while left < right:
            
            SecondNum = nums[left]
            ThirdNum = nums[right]

            PotentialClosest = FirstNum+SecondNum+ThirdNum
            if abs(PotentialClosest - target) < abs(closest - target):
                closest = PotentialClosest
            if PotentialClosest > target:
                right -= 1
            elif PotentialClosest < target:
                left += 1
            else:
                closest = PotentialClosest
                left += 1
                right -= 1
    return closest


print(foo(nums, target))
    

