roman = {"I": 1, "V" : 5 , "X" : 10, "L" : 50,
          "C" : 100, "D" : 500, "M" : 1000}
ahh = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90,
       "CD" : 400, "CM" : 900 }
add = 0
rom_inp = input("Please write a roman number: ")
temp = ""
temp2 = ""
for pos, i in enumerate(rom_inp):
    temp += i
    if len(temp) < 2:
        continue
    elif len(temp) == 2:
        if temp in ahh:
            add += ahh.get(temp)
            temp = temp.replace(temp,"",1)
            continue
        else:
            temp2 += temp[0]
            temp = temp.replace(temp[0],"",1)
            continue
    elif len(temp) > 2:
        for j in temp:
            temp = temp.replace(temp[0], "",1)
temp2 += temp
for i in temp2:
    if i in roman:
        add += roman.get(i)
print(add)