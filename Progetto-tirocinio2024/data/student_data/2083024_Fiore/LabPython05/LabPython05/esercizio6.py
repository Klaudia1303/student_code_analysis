s = input("inserisci una stringa: ")
max =0
for i in range(len(s)):
    distanza = s.rfind(s[i])-i
    
    if distanza > max:
        max = distanza
        print(s[i], distanza)

    
