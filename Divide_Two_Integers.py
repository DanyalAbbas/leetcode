dividend = 10
divisor = 3

def foo(dividend : int, divisor : int) -> int:
    answer = 0
    a, b = abs(dividend), abs(divisor)
    negative = (dividend>0 and divisor<0) or (dividend<0 and divisor>0)

    while a >= b:
        counter = 1
        decrement = b
        while a >= decrement:
            answer += counter
            a = a-decrement
            decrement += decrement
            counter += counter
            
    answer = answer if not(negative) else -answer

    return min(max(-2147483648, answer), 2147483647)


print(foo(dividend, divisor))

