words = ["abc","car","ada","racecar","cool"]

def foo(words : list):
    for i in words:
        if i[::-1] == i:
            return i
    return ""


print(foo(words))