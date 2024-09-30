str1 = "ABCABCABC"
str2 = "ABCAAA"

import math

def foo(str1 : str, str2 : str) -> str:
    if str1 + str2 == str2 + str1:
        length = math.gcd(len(str1), len(str2))
        return str1[:length]
    else:
        return ""
    

print(foo(str1, str2))