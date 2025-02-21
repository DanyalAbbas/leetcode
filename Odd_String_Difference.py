words = ["ddd","poo","baa","onn"]

def foo(words: list[str]) -> str:
    Difference = []
    for i in words:
        l = []
        for j in range(len(i) -1):
            l.append(ord(i[j+1]) - ord(i[j]))
        Difference.append(l)
    
    for i in range(len(Difference)):
        if Difference.count(Difference[i]) == 1:
            return words[i]


print(foo(words))
            

