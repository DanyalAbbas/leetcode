arr = [17,18,5,4,6,1]

def foo(arr : list[int]) -> list[int]:
    maxNum = arr.index(max(arr))
    for i in range(len(arr) -1):
        if i < maxNum:
            arr[i] = arr[maxNum]
        else:
            maxNum = arr.index(max(arr[i+1::]))
            arr[i] = arr[maxNum]
    arr[-1] = -1
    return arr

print(foo(arr))

