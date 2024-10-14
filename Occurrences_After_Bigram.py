text = "alice is a good girl she is a good student"
first = "a"
second = "good"

def foo(text : str, first : str, second : str) -> list[str]:
    text = text.split()
    third = []
    for i in range(len(text) - 2):
        if text[i] == first and text[i+1] == second:
            third.append(text[i+2])
    return third
    

print(foo(text, first, second))