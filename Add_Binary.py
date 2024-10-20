a = "11"
b = "1"


def foo(a : str, b : str) -> str:
    answer = ""
    extra1 = ["0" for i in range(1,len(a)) if len(b) < len(a)]
    extra2 = ["0" for i in range(1,len(b)) if len(a) < len(b)]
    a = "".join(extra2) + a
    b = "".join(extra1) + b
    carry = 0
    for x, y in zip(list(a)[::-1], list(b)[::-1]):
        added = int(x) + int(y) + carry

        if added == 2:
            carry = 1
            answer += "0"
        elif added == 3:
            carry = 1
            answer += "1"
        else:
            carry = 0
            answer += str(added)
    
    if carry > 0:
        answer += str(carry)

    return answer[::-1]


print(foo(a,b))
