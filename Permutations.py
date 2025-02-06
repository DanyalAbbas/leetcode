nums = [1,2,3]

def foo(nums : list[int]) -> list[list[int]]:
    l = []
    for i in range(len(nums)):
        hmm = nums[:]
        j = 0
        while j < len(hmm):
            hmm.append(hmm.pop(i))
            l.append(list(hmm))
            j += 1
            
    return l

print(foo(nums))