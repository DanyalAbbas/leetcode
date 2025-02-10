arr = [6,4,5,0,5,8,2,7,2]

def foo(arr : list[int]) -> list[int]:
    new = arr[:]
    if 0 in arr:
        index = arr.index(0)
        for i in range(arr.count(0)):
            new.insert(index, 0)
            if 0 not in arr[index+2::] or len(arr) == index+1: break
            else:
                index = new.index(0, index+2)

    for i in range(len(arr)):
        arr[i] = new[i]
    print(arr)



foo(arr)