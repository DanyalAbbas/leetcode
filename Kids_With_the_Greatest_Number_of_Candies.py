candies = [2,3,5,1,3]
extraCandies = 3

def foo(candies : list[int], extraCandies : int) -> list[bool]:
    NewCandies = []
    for i in candies:
        if max(i+extraCandies, max(candies)) == i+extraCandies:
            NewCandies.append(True)
        else:
            NewCandies.append(False)
    return NewCandies


print(foo(candies, extraCandies))
            