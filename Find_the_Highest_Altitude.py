gain = [-5,1,5,0,-7]

def foo(gain : list[int]) -> int:
    Altitudes = [0]
    for i in range(len(gain)):
        Altitudes.append(gain[i]+Altitudes[-1])
    
    return max(Altitudes)


print(foo(gain))