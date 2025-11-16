sentence = "I speak Goat Latin"

def foo(sentence: str):
    l = sentence.split()
    for i in range(len(l)):
        if l[i][0] not in 'aeiouAEIOU':
            l[i] = l[i][1::] + l[i][0]
        
        l[i] += 'ma'
        l[i] += 'a'*(i+1)

    return ' '.join(l)

print(foo(sentence))


