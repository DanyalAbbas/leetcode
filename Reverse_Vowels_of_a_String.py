s = "IceCreAm"

def foo(s : str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    VowelsInS = [s[i] for i in range(len(s)) if s[i].lower() in vowels]
    s1 = list(s)
    count = 0
    for pos, i in enumerate(s[::-1]):
        if i.lower() in vowels:
            s1[len(s) - 1 - pos] = VowelsInS[count]
            count += 1
    return "".join(s1)

print(foo(s))
