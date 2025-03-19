strs = ["eat","tea","tan","ate","nat","bat"]

def foo(strs : list[str]) -> list[list[str]]:
    Anagrams = {}
    for i in range(len(strs)):
        val =  sorted(strs[i])
        if Anagrams:
            if "".join(val) in Anagrams.keys():
                Anagrams["".join(val)].append(strs[i])
            else:
                Anagrams["".join(val)] = [strs[i]]
        else:
            Anagrams["".join(val)] = [strs[i]]
    return list(Anagrams.values())


print(foo(strs))
        

