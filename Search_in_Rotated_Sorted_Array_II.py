nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2

def foo(nums : list[int], target : int) -> bool:
    # index = nums.index(min(nums))
    # nums = nums[index:] + nums[:index]


    # start = 0
    # end = len(nums) -1
    # while start <= end:
    #     MidVal = nums[(start+end)//2]
    #     if MidVal == target:
    #         return True
        
    #     if MidVal > target:
    #         end = ((start+end)//2) - 1
        
    #     if MidVal < target:
    #         start = ((start+end)//2) + 1

    # return False

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return True

        if nums[l] == nums[mid]:
            l += 1
        elif nums[l] < nums[mid]:
            if nums[l] <= target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
    return False


print(foo(nums, target))