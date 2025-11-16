widths = [3,4,10,4,8,7,3,3,4,9,8,2,9,6,2,8,4,9,9,10,2,4,9,10,8,2]
s = "mqblbtpvicqhbrejb"


def foo(widths : list[int], s : str) -> list[int]:
    n1 = 0
    n2 = 1
    count = 0
    size = len(s)
    while count < size:
        n1 += widths[ord(s[count]) - 97]
        if n1 == 100 and count != size-1:
            n2 += 1
            n1 = 0
        elif n1 > 100:
            n2 += 1
            n1 = 0
            continue
        count += 1

    return [n2,n1] 
    

print(foo(widths, s))
