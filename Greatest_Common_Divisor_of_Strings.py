str1 = "ABCABCABC"
str2 = "ABC"

import math

# With math.gcd()
def foo(str1 : str, str2 : str) -> str:
    if str1 + str2 == str2 + str1:
        length = math.gcd(len(str1), len(str2))
        return str1[:length]
    else:
        return ""

# Without math.gcd()
def bar(str1 : str, str2 : str) -> str:
    minimum_length = min(len(str1), len(str2))
    for i in range(minimum_length, 0, -1):
        if len(str1) % i == 0 and len(str2) % i == 0:
            candidate = str1[:i]
            if candidate * (len(str1) // i) == str1 and candidate * (len(str2) // i) == str2:
                return candidate[:i]
    return ""



print(foo(str1, str2))
print(bar(str1, str2))