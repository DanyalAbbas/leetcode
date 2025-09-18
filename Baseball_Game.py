operations = ["5","2","C","D","+"]

def foo(operations: list[str]) -> int:
    stack = []
    for i in operations:
        if i not in ["+", "C", "D"]:
            stack.append(int(i))
        elif i == "+":
            stack.append(int(stack[-2]) + int(stack[-1]))
        elif i == "C":
            stack.pop()
        else:
            stack.append(int(stack[-1])*2)
    return sum(stack)

print(foo(operations))