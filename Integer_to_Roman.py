num = 3749

def foo(num : int):
      roman = {1 : "I", 4 : "IV", 5 : "V" , 9 : "IX", 10 : "X", 40 : "XL", 50 : "L",
           90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M"}        
      
      temp = ""
      for i in range(100):
            if num == 0:
                  break
            k = list(roman.keys())
            for i in k.copy():
                  if i > num:
                        k.remove(i)
            print(num)
            print(k)
            num -= max(k)
            temp += roman.get(max(k))
      return temp


print(foo(num))