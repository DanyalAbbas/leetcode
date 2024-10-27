rec1 = [0,0,2,2]
rec2 = [1,1,3,3]


def foo(rec1 : list[int], rec2 : list[int]) -> bool:
    return rec1[0] < rec2[2] and rec1[1] < rec2[3] and rec1[2] > rec2[0] and rec1[3] > rec2[1]


print(foo(rec1, rec2))