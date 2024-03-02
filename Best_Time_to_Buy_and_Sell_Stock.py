prices = [7,1,5,3,6,4]

import time

def foo(prices : list):
    min_num = prices[0]
    max_num = 0
    for i in prices[1::]:
        max_num = max(max_num, i - min_num)
        min_num = min(min_num, i)
        
    return max_num
    

t1 = time.time()
print(foo(prices))
t2 = time.time()
print(t2-t1)