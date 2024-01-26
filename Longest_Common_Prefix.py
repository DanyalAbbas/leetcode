strs = ["flower", "flosing", "flowing"]
chars = zip(*strs)
pre = ""
for i in chars:
    if len(set(i)) == 1:
        pre += i[0]
    else:
        break
print(pre)