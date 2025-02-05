nums = [1,2,3]

def foo(nums : list[int]) -> list[list[int]]:
    PowerSet = [[]]
    for element in nums:
        new_subsets = []
        for subset in PowerSet:
            new_subsets.append(subset + [element]) 
        PowerSet.extend(new_subsets)
    return PowerSet


print(foo(nums))