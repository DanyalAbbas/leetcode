n = 4

def foo(n : int) -> list[str]: # couldnt solve this one >:(
    res = []
    def dfs(openP, closeP, s):
        if openP == closeP and openP + closeP == n * 2:
            res.append(s)
            return
        
        if openP < n:
            dfs(openP + 1, closeP, s + "(")
            
        if closeP < openP:
            dfs(openP, closeP + 1, s + ")")

    dfs(0, 0, "")

    return res


print(foo(4))
