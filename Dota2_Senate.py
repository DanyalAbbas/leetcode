senate = "RDD"

def foo(senate : str) -> str:
    senate = list(senate)
    RadiantCount = senate.count("R")
    DireCount = senate.count("D")
    i = 0
    while (DireCount != len(senate)) or (RadiantCount != len(senate)):
        print(senate)
        if senate[i] == "D":
            if DireCount == len(senate):
                return "Dire"
            else:
                senate.append(senate.pop(0))
                senate.remove("R")
                i -= 1
                RadiantCount -= 1
        else: 
            if RadiantCount == len(senate):
                return "Radiant"
            else:
                senate.append(senate.pop(0))
                senate.remove("D")
                i -= 1
                DireCount -= 1
        i +=1
            

print(foo(senate))
