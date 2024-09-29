import string
k = 10


def foo(k : int) -> str:
    word = "a"
    for i in range(k):
        if len(word) > k:
            break
        word_copy = word
        for i in word_copy:
            word += string.ascii_lowercase[string.ascii_lowercase.find(i) + 1]
    return word[k-1]

    

print(foo(k))