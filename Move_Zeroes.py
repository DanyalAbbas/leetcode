nums = [0,0,1,2]

def foo(nums : list[int]):
    i = 0
    
    
    while i < len(nums) - nums.count(0):
        print(i)
        if nums[i] == 0:
            nums.append(nums.pop(i))
            i -= 1
        i += 1

print(nums)
foo(nums)
print(nums)