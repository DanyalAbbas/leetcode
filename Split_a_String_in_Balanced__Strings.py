s = "RLRRLLRLRL"

def foo(s : list[str]) -> int:
    SubStringCount = 0
    TempString = ""
    for i in s:
        TempString += i
        if TempString.count("R") == TempString.count("L"):
            SubStringCount +=1
            TempString = ""
    return SubStringCount

print(foo(s))
