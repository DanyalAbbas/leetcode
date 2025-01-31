s = "weallloveyou"
k = 7

def foo(s : str, k : int) -> int:
    Vowels = ["a","e","i","o","u"]
    SubstringLength = 0
    for i in s[0:k]:
        if i in Vowels: SubstringLength += 1
    count = SubstringLength
    i = 1
    while i <= len(s) - k:
        thingey = s[i:i+k]
        if s[i-1] in Vowels:
            count -= 1
        if s[i+k-1] in Vowels:
            count += 1
        SubstringLength = max(count, SubstringLength)
        i += 1
    return SubstringLength

print(foo(s,k))

