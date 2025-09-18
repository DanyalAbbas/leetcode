tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def foo(tokens : list[str]) -> int:
    stack = []
    for i in tokens:
        if i not in "+-*/":
            stack.append(i)
        elif i in "+-*/":
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(int(eval(f"{val1} {i} {val2}")))
    return stack[-1]

foo(tokens)


