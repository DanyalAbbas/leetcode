n = 3

def foo(n : int) -> str:
    RLE_string = "1"
    count = 1
    while count < n:
        temp = ""
        i = 0
        while i < len(RLE_string):
            smt = RLE_string[i]
            if i == (len(RLE_string) -1) or RLE_string[i+1] != smt:
                temp += str(i+1) + smt
                i = 0
                RLE_string = RLE_string.lstrip(smt)
                continue
            i += 1
        RLE_string = temp
        count += 1
    return RLE_string
    

print(foo(n))