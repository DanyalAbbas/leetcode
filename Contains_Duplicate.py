nums = [1,2,3,1]

def foo(nums : list):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True

print(foo(nums))