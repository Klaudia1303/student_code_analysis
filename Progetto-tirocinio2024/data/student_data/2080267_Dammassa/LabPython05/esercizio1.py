s = input("inserisci stringa: ")
s1 = input("inserisci un altra string stessa lunghezza: ")
h = 0
if len(s) == len(s1):
    for i in range(0, len(s)):
            print(s[i]+s1[h], end= "")
            h +=1
else:
    print("Stringhe di diversa lunghezza")
    
