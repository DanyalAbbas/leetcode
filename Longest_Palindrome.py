
s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

def foo(s : str) -> int:
    Odd = -1
    UniqueVals = set(s)
    MaxLength = 0
    Oddlist = []
    for i in UniqueVals:
        countVal = s.count(i)
        if countVal % 2 == 0:
            MaxLength += countVal
        elif countVal % 2 == 1:
            if countVal < Odd:
                Oddlist.append(countVal)
            else:
                if Odd != -1:
                    Oddlist.append(Odd)
                Odd = countVal
    

        
    if Odd != -1: MaxLength += Odd

    MaxLength += sum(Oddlist) - len(Oddlist)
    
    return MaxLength

print(foo(s))

