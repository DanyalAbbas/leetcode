s = "a "

count = 0
for pos, i in enumerate(s[::-1]):
    if i == " ":
        continue
    else:
        count += 1
        if len(s) == 1:
            break
        else:
            if pos+1 == len(s) or s[::-1][pos+1] == " ":
                break
    
print(count)