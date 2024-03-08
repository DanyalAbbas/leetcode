haystack = "mississippi"
needle = "issip"

def sol(haystack : str, needle : str):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

print(sol(haystack, needle))

