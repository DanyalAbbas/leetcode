startTime = [1,2,3]
endTime = [3,2,7] 
queryTime = 4

def foo(startTime : list[int], endTime : list[int], queryTime : int) -> int:
    Count = 0
    i = 0
    while i < len(startTime):
        if queryTime > startTime[i] and queryTime < endTime[i]:
            Count += 1
        i +=1
    return Count

print(foo(startTime, endTime, queryTime))