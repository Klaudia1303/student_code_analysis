s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
l_max=0
for i in range(len(s1)+1):
    for j in range(i+1, len(s1)+1):
        s=s1[i:j]
        if(s in s2):
            lunghezza=j-i
            if(lunghezza>l_max):
                stringa=s
                l_max=lunghezza
        else:
            break
print(stringa)
