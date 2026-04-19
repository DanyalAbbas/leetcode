import string
words = ["gin","zen","gig","msg"]


def foo(words : list[str]) -> int:
    unique = set()

    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alphabet = list(string.ascii_lowercase)
    concat = dict(zip(alphabet, morse_code))

    for i in words:
        new = ''
        for j in i:
            new += concat[j]
        unique.add(new)
        new =''

    return len(unique)  

print(foo(words))