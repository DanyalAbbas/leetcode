arr = [2,1]

def foo(arr : list[int]):
    if len(arr) <= 2:
        return False
    
    maxNum = arr.index(max(arr))

    if arr.count(arr[maxNum]) > 1:
        return False

    arr1, arr2 = arr[:maxNum], arr[maxNum+1:]

    if len(arr1) != len(set(arr1)) or len(arr2) != len(set(arr2)):
        return False


    if arr1 and arr2:
        if (sorted(arr1) == arr1) and (sorted(arr2, reverse=True) == arr2):
            return True
        else:
            return False
    else:
        return False
    

print(foo(arr))