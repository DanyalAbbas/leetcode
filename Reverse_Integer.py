x = 120
def foo(x : int) -> int:
    Converted_Value = 0
    if x < 0:
        Converted_Value = int(str(x)[1:][::-1]) * -1
    else:
        Converted_Value = int(str(x)[::-1])

    if Converted_Value > 2 ** 31 - 1 or Converted_Value < -2 ** 31:
        return 0
    return Converted_Value

print(foo(x))