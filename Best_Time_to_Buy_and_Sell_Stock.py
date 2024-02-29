prices = [7,1,5,3,6,4]

import time

def foo(prices : list):
    temp = 0
    num = 0
    pos2 = 0
    for pos1, i in enumerate(prices):
        for j in prices[pos1+1::]:
            if j < i:
                num = j
                pos2 = pos1+2
                break
            # print(f"{j} - {i}")
            if (j - i) > temp:
                temp = j-i
        if (max(prices[pos2::]) - num) > temp:
            print(f"{max(prices[pos2::])} - {num} > {temp} ")
            temp = max(prices[pos2::]) - num
            
    
    return temp

t1 = time.time()
print(foo(prices))
t2 = time.time()
print(t2-t1)