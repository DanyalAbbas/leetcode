heights  = [1,1,4,2,1,3]
expected = [1,1,1,2,3,4]

def foo(heights : list):
    expected = sorted(heights)
    num = 0
    t = zip(heights, expected)
    for i in t:
        if len(set(i)) == 1:
            pass
        else:
            num += 1
    return num


print(foo(heights))

