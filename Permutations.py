nums = [1,2,3]

def foo(nums : list[int]) -> list[list[int]]:
    if len(nums) == 1:
        return [nums[:]]
    
    res = []

    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = foo(nums)
        
        print(perms)
        for p in perms:
            p.append(n)
            
        res.extend(perms)
        nums.append(n)
        
    return res

print(foo(nums))