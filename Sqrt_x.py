x = 2

def sol(x):
    temp = 0
    if x == 0 or x == 1:
        print("huh")
        return x
    else:
        for i in range(1,x+1):
            temp = i-1
            if i*i == x:
                return i
            elif i*i > x:
                return temp

print(sol(x))
