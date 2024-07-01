pattern = "abba"
s = "dog cat cat dog"

def foo(pattern : str, s : str):
    for i in zip(pattern,s.split()):
        print(i)

foo(pattern,s)