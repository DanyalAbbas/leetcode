haystack = "mississippi"
needle = "issip"

ind = 0
if needle in haystack:
    ind = haystack.index(needle)
    j = haystack.rstrip(needle)
    if needle in j:
        ind = j.index(needle)
        print(ind)
    else:
        print(ind)
else:
    print(-1)

