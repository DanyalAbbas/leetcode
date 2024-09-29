celsius = 36.50

def foo(celsius : float) -> list:
    return [celsius + 273.15, celsius * 1.80 + 32.00]
    

print(foo(celsius))