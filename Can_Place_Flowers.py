flowerbed = [0,0,1,0,0]
n = 1

def foo(flowerbed : list, n : int):
    temp = 0
    if n == 0:
        return True
    for pos,i in enumerate(flowerbed):
        if i == 0 and (pos == 0 or flowerbed[pos-1] == 0) and (pos == len(flowerbed) - 1 or flowerbed[pos+1] == 0):
            flowerbed.pop(pos)
            flowerbed.insert(pos, 1)
            temp += 1
            if n == temp:
                return True
    return False
    
print(foo(flowerbed, n))