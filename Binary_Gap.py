n = 13

def foo(n : int) -> int:
    s = format(n, "b")
    print(s)
    if s.count("1") > 1:
        count = 0
        start = s.find("1")
        end = s.find("1", start+1)
        while end != -1:
            count = max(count, end - start)
            start = s.find("1", start +1)
            end = s.find("1", end+1)
        return count
    else:
        return 0
 

print(foo(n))