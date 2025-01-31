senate = "RDD"

def foo(senate : str) -> str:
    senate = list(senate)
    r = senate.count("R")
    d = senate.count("D")
    i = 0
    while (d != len(senate)) or (r != len(senate)):
        print(senate)
        if senate[i] == "D" and d == len(senate):
            return "Dire"
        elif senate[i] == "D":
            senate.append(senate.pop(0))
            senate.remove("R")
            i -= 1
            r -= 1
        elif senate[i] == "R" and r == len(senate):
            return "Radiant"
        elif senate[i] == "R":
            senate.append(senate.pop(0))
            senate.remove("D")
            i -= 1
            d -= 1
        i +=1
            

print(foo(senate))
