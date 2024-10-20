digits = "23"

digit_to_letters = {
            "1" : [""],
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
}

def foo(digits : str, hashmap : dict) -> list[str]:
    
    if not digits:
        return []
    
    All_Outputs = []
    l = []
    i = 0

    def backtrack(i):
        nonlocal All_Outputs
        nonlocal l
        if i == len(digits):
            All_Outputs.append("".join(l))
            return
        
        for j in digit_to_letters[digits[i]]:
            l.append(j)
            backtrack(i+1)
            l.pop(-1)
        
    
    backtrack(i)
    return All_Outputs
    
            


print(foo(digits, digit_to_letters))

