arr = [1,2,2,1,1,3]

def foo(arr : list[int]) -> bool:
    arr = [arr.count(i) for i in set(arr[:])]
    return len(set(arr)) == len(arr)


print(foo(arr)) 