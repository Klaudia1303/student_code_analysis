s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
massimo=0
for i in s1:
    c=""
    if i in s2:
        c=c+i
        x=s1.find(i)
        y=s2.find(i)
        for j in s1[x+1:]:
            if y<len(s2)-1:
                if j==s2[y+1]:
                    c=c+j
                else:
                    break
            else:
                break
            y=y+1
        if len(c)>massimo:
            massimo=len(c)
            b=c

print(b)
    
