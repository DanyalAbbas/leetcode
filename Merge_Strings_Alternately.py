word1 = "abcd"
word2 = "pq"


def foo(word1 : str, word2 : str) -> str:
    minimum = min(len(word1), len(word2))
    NewString = ""
    for i in range(minimum):
        NewString += word1[i] + word2[i]
    NewString += (word1 if len(word1) > minimum else word2)[minimum:] 
    return NewString

print(foo(word1, word2))

