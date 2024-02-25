nums = [1]
target = 1

def foo(nums : list, target : int):
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = (start+end)//2
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return start
    

print(foo(nums, target)) 



    